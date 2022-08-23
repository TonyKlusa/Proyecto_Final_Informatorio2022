from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import Noticia, Categoria, Comentario

# Create your views here.
def index(request):
    return render (request, 'base.html')

def nosotros(request):
    return render (request, 'nosotros.html')

def eventos(request):
    return render (request, 'eventos.html')

def noticias(request):
    return render (request, 'noticias/noticias.html')

def donaciones(request):
    return render (request, 'donaciones.html')

def login(request):
    return render (request, 'login.html')



