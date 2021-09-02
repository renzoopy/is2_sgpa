from os import name
from django.contrib import admin
from django.urls import path, include
from .views import CrearPerfil, editarPerfil, home


urlpatterns = [
    path("", home, name="home"),
    path("perfil_form/", CrearPerfil.as_view(), name="perfil_form"),
    path("editar_perfil/<int:id_perfil>/", editarPerfil, name="editar_perfil"),
]
