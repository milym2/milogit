from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def prueba(request):
	externo = open("C:/Users/USER/Desktop/examen/milo/templates/index.html")
	plantilla = Template(externo.read())
	externo.close()
	ctx = Context()
	contenido = plantilla.render(ctx)
	return HttpResponse(contenido)