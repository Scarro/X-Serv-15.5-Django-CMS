from django.shortcuts import render
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import Pages

# Create your views here.


@csrf_exempt
def index(request):
    template = "cms/basesite.html"
    context = {
        'pages':Pages.objects.all()
    }
    return render(request, template, context)

def agregar(request, nombre, recurso):
    try:
        Pages.objects.get(nombre=nombre)
    except (KeyError, Pages.DoesNotExist):
        Pages.objects.create(nombre=nombre, recurso=recurso)
    context = {
        'pages':Pages.objects.all()
    }
    return render(request, 'cms/basesite.html', context)