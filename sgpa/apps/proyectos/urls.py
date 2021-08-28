from os import name
from django.contrib import admin
from django.urls import path, include
from .views import base, nuevoProyecto, home

urlpatterns = [
    path('',base,name="base"),
    path('home/',home,name="home"),
    path('nuevo/',nuevoProyecto,name="nuevoProyecto"),
]