from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check', views.check, name='check'),
    path('ontology.ttl', views.ontology, name='ontology'),
    path('shapes.ttl', views.shapes, name='shapes'),
    path('validate', views.validate, name='validate'),
]