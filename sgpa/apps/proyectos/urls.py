from os import name
from django.contrib import admin
from django.urls import path, include

from .views import home, proy, ProyectoListar, ProyectoCrear

urlpatterns = [
    path("", proy, name="proy"),
    path("home/", home, name="home"),
    path("nuevo/", ProyectoCrear.as_view(), name="nuevo_proyecto"),
    path("listar_proyectos/", ProyectoListar.as_view(), name="listar_proyectos"),
]
