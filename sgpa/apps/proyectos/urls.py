from os import name
from django.contrib import admin
from django.urls import path, include
from .views import nuevoProyecto, home, proyectos

urlpatterns = [
    path('',proyectos,name="proyectos"),
    path('home/',home,name="home"),
    path('nuevo/',nuevoProyecto,name="nuevoProyecto"),
]