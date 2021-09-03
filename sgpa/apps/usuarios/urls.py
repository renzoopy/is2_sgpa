from os import name
from django.contrib import admin
from django.urls import path, include
from .views import CrearPerfil, ListarPerfil, editarPerfil, home


urlpatterns = [
    path("", home, name="home"),
    path("nuevo/", CrearPerfil.as_view(), name="crear_form"),
    path("listar/", ListarPerfil.as_view(), name="listar_perfiles"),
    path("editar_perfil/<int:id_perfil>/", editarPerfil, name="editar_perfil"),
]
