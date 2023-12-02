from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> Hola Mundo con Django 🐴</h1>')

def get_movies(request):
      return HttpResponse('<h2> Listado de peliculas</h2>')