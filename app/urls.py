from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('movies/', views.index,name= 'inicio_app'),
    path('getmovies/', views.get_movies,name= 'getmovies_app'),
]

