from os import name
from django.contrib import admin
from django.urls import path, include

from .views import crearProyecto, home, listarProyectos, proy

urlpatterns = [
    path("", proy, name="proy"),
    path("home/", home, name="home"),
    path("nuevo/", crearProyecto.as_view(), name="nuevo_proyecto"),
    path("listar/", listarProyectos.as_view(), name="listar_proyectos"),
]
