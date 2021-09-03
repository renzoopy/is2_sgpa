from os import name
from django.contrib import admin
from django.urls import path, include

from .views import nuevoProyecto, home, proy, ProyectoListar

urlpatterns = [
    path("", proy, name="proy"),
    path("home/", home, name="home"),
    path("nuevo/", nuevoProyecto, name="nuevo_proyecto"),
    path("listar_proyectos/", ProyectoListar.as_view(), name="listar_proyectos"),
]
