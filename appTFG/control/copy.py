from shutil import copyfile
from TFG.settings import (url_mydocumentation, url_static, url_resources, url_ontology, url_index, index1)

# Funcion para copiar ficheros creados por widoco en nuestra aplicacion utilizando la libreria shutil y la funcion copyfile
def copyFiles():

# Se copian los ficheros index y ontology en templates
# Los ficheros css y js los copiamos en otro directorio creado, static
    copyfile(url_mydocumentation + index1, url_index)
    copyfile(url_mydocumentation + 'ontology.ttl', url_ontology)
    copyfile(url_resources + 'primer.css', url_static + 'primer.css')
    copyfile(url_resources + 'extra.css', url_static + 'extra.css')
    copyfile(url_resources + 'rec.css', url_static + 'rec.css')
    copyfile(url_resources + 'owl.css', url_static + 'owl.css')
    copyfile(url_resources + 'jquery.js', url_static + 'jquery.js')
    copyfile(url_resources + 'marked.min.js', url_static + 'marked.min.js')