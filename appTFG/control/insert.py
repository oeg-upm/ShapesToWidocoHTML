from bs4 import BeautifulSoup
from TFG.settings import (url_index)

# Creacion de funcion para insertar codigo html en el index copiado en templates
def insertCode():


# Con la libreria soup se abre el fichero index de templates
    soup = BeautifulSoup(open(url_index), 'html.parser')

# Eliminar los link y script que vamos a insertar después
    soup.find("script", {"src": "resources/jquery.js"}).extract()
    soup.find("script", {"src": "resources/marked.min.js"}).extract()

    soup.find("link", {"href": "resources/primer.css"}).extract()
    soup.find("link", {"href": "resources/rec.css"}).extract()
    soup.find("link", {"href": "resources/extra.css"}).extract()
    soup.find("link", {"href": "resources/owl.css"}).extract()

# Se introduce primer link a un css con sus atributos en head con append que lo mete al final
    new_link = soup.new_tag('link')
    new_link.attrs['rel'] = 'stylesheet'
    new_link.attrs['href'] = '{% static \'extra.css\' %}'  # static
    soup.head.append(new_link)

    new_link = soup.new_tag('link')
    new_link.attrs['rel'] = 'stylesheet'
    new_link.attrs['href'] = '{% static \'owl.css\' %}'
    soup.head.append(new_link)

    new_link = soup.new_tag('link')
    new_link.attrs['rel'] = 'stylesheet'
    new_link.attrs['href'] = '{% static \'primer.css\' %}'
    soup.head.append(new_link)

    new_link = soup.new_tag('link')
    new_link.attrs['rel'] = 'stylesheet'
    new_link.attrs['href'] = '{% static \'rec.css\' %}'
    soup.head.append(new_link)

    new_link = soup.new_tag('link')
    new_link.attrs['rel'] = 'stylesheet'
    new_link.attrs['href'] = '{% static \'validate.css\' %}'
    soup.head.append(new_link)

# Se introduce el script que modifica tabla de contenidos y se mete con insert al principio, es esencial que se ejecute antes
    new_script = soup.new_tag('script')
    new_script.attrs['type'] = 'text/javascript'
    new_script.attrs['src'] = '{% static \'jquery.js\' %}'
    soup.head.insert(1, new_script)

# Se introduce script para el css
    new_script = soup.new_tag('script')
    new_script.attrs['type'] = 'text/javascript'
    new_script.attrs['src'] = '{% static \'marked.min.js\' %}'
    soup.head.insert(3, new_script)

# Se introduce nuestro script para añadir la funcion de validacion
    new_script = soup.new_tag('script')
    new_script.attrs['type'] = 'text/javascript'
    new_script.attrs['src'] = '{% static \'validate.js\' %}'
    soup.head.insert(4, new_script)

# Se introduce script con la libreria ajax para utilizar en nuestro script de validacion... esencial ponerlo al principio porque si no no carga bien el script
    new_script = soup.new_tag('script')
    new_script.attrs['src'] = 'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'
    soup.head.insert(2, new_script)

# Aqui se empieza a meter la parte para descargar las shapes, desde dentro hacia fuera
    new_img = soup.new_tag('img')
    new_img.attrs['src'] = 'https://img.shields.io/badge/Format-TTL-blue.svg'
    new_img.attrs['<'] = ''
    new_img.attrs['img'] = ''

    new_a = soup.new_tag('a')
    new_a.attrs['href'] = 'shapes.ttl'
    new_a.attrs['target'] = '_blank'
    new_a.append(new_img)

    new_span = soup.new_tag('span')
    new_span.append(new_a)

    new_dd = soup.new_tag('dd')
    new_dd.append(new_span)

    new_dt = soup.new_tag('dt')
    new_dt.string = "Download shapes"

    new_dl = soup.new_tag('dl')
    new_dl.insert(0, new_dt)
    new_dl.insert(1, new_dd)

    new_br = soup.new_tag('br')

    soup.find("dt", text="Download serialization:").parent.insert_after(new_dl)

# Aqui se empieza a meter la parte de validacion, otra vez desde dentro hacia fuera
    new_text = soup.new_tag('textarea')
    new_text.attrs['id'] = 'textrules'
    new_text.attrs['rows'] = '14'
    new_text.attrs['cols'] = '60'
    new_text.attrs['placeholder'] = 'This is a placeholder where the rules should be explained in natural language.'

    new_h4 = soup.new_tag('h4')
    new_h4.string = 'Validation rules'

    new_button = soup.new_tag('button')
    new_button.attrs['class'] = 'buttonS'
    new_button.attrs['onclick'] = "validate('{% url 'validate'%}', '{{ csrf_token }}')"
    new_button.string = 'Validate'

    new_text1 = soup.new_tag('textarea')
    new_text1.attrs['id'] = 'textdata'
    new_text1.attrs['rows'] = '14'
    new_text1.attrs['cols'] = '100'
    new_text1.attrs['placeholder'] = 'Write data for the validation. Only Turtle format (ttl) is supported.'

    new_input = soup.new_tag('input')
    new_input.attrs['class'] = 'inp'
    new_input.attrs['type'] = 'checkbox'

    new_label = soup.new_tag('label')
    new_label.attrs['id'] = 'labelValid'
    new_label.string = 'Coverage'
    new_label.append(new_input)

    new_br = soup.new_tag('br')
    new_br1 = soup.new_tag('br')
    new_br2 = soup.new_tag('br')
    new_br3 = soup.new_tag('br')

    new_span1 = soup.new_tag('span')
    new_span1.attrs['class'] = 'spanExp'
    new_span1.attrs['style'] = 'color:#87CEFA'
    new_span1.string = '*'

    new_span2 = soup.new_tag('span')
    new_span1.attrs['class'] = 'spanExp'
    new_span2.string = 'Coverage parameter specifies, if true, which types within the data are covered by the provided shape (consider that those not covered by the shape are always correctly validated).'

    new_divValid = soup.new_tag('div')
    new_divValid.attrs['id'] = 'divValid'
    new_divValid.append(new_label)
    new_divValid.append(new_br1)
    new_divValid.append(new_span1)
    new_divValid.append(new_span2)
    new_divValid.append(new_br)
    new_divValid.append(new_br2)
    new_divValid.append(new_text1)
    new_divValid.append(new_br3)
    new_divValid.append(new_button)


    new_a = soup.new_tag('a')
    new_a.attrs['href'] = '#toc'
    new_a.string = 'ToC'

    new_span = soup.new_tag('span')
    new_span.attrs['class'] = 'backlink'
    new_span.string = 'back to'
    new_span.append(new_a)

    new_h2 = soup.new_tag('h2')
    #new_h2.attrs['id'] = 'valid'
    new_h2.attrs['class'] = 'list'
    new_h2.string = 'Validation'
    new_h2.append(new_span)

# Se mete el div con el resto incluido, importante incluirselo en orden. Al final se añade al body con soup
    new_div = soup.new_tag('div')
    new_div.attrs['id'] = 'validation'
    new_div.append(new_h2)
    new_div.append(new_divValid)
    new_div.append(new_h4)
    new_div.append(new_text)
    soup.find("div", {"id": "references"}).insert_before(new_div)

# Se escribe el codigo añadido en el index de templates para actualizarlo
    with open(url_index, "w") as file:
        file.write(str(soup))