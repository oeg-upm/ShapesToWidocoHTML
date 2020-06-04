from TFG.settings import (url_index, url_shapes, url_ontology, url_api, index1)
from django.shortcuts import render, redirect
from appTFG.control.copy import copyFiles
from appTFG.control.insert import insertCode
from django.http import HttpResponse, JsonResponse
import requests
import json
import os.path

# Create your views here.
def index(request) :

    copyFiles()

    with open(url_index, 'r') as original: data = original.read()
    with open(url_index, 'w') as modified: modified.write("{% load static %}\n" + data)


    insertCode()


    with open(url_ontology, 'r') as file:
        ontology = file.read()
        file.close()

    headers = {'content-type': 'application/json'}
    data1 = {
        "ontology": ontology,
        "serialisation": 'TURTLE'
    }

    response = requests.post(url_api, data= json.dumps(data1), headers= headers)
    with open(url_shapes, 'w+') as file:
        file.write(response.text)
        file.close()

    return render(request, index1)


def check(request):
    return render(request, index1)


def ontology(request):

    if (os.path.exists(url_ontology)):
        with open(url_ontology, 'r') as file:
            return HttpResponse(file.read(), content_type= 'text/plain')
    return redirect('index')


def shapes(request):

    if (os.path.exists(url_shapes)):
        with open(url_shapes, 'r') as file:
            return HttpResponse(file.read(), content_type='text/plain')
    return redirect('index')


def validate(request):

    try:
        json_response = json.loads(request.body)
    except Exception as e:
        response_json = {"data": e.args[0]}
        response1 = JsonResponse(response_json)
        response1.status_code = 400
        return response1

    with open(url_shapes, 'r') as file:
        shape = file.read()
        file.close()

    headers = {'content-type': 'application/json'}

    coverage = False
    if (json_response['coverage']):
        coverage = True

    if len(json_response['dataValid'])==0:
        response_json = {"data": ""}
        response1 = JsonResponse(response_json)
        response1.status_code = 200
        return response1

    payload = {"coverage": coverage,
        "data": json_response['dataValid'],
        "dataFormat": 'Turtle',
        "shape": shape,
        "shapeFormat": 'Turtle'
        }
    response = requests.post('https://astrea.linkeddata.es/api/validation/document', data=json.dumps(payload), headers=headers)
    if len(response.content.decode('utf-8'))==0:
        response_json = {"data": "Data not compatible with shape"}
    else:
        response_json = {"data": response.content.decode('utf-8')}
    response1 = JsonResponse(response_json)
    response1.status_code = response.status_code
    return response1