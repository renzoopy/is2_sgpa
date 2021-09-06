from os import name
from django.contrib import admin
from django.urls import path, include
from .views import (
    CrearPerfil,
    ListarPerfil,
    administrador,
    concederAcceso,
    editarPerfil,
    eliminarPerfil,
    home,
    listaAcceso,
    proyectos_usuario,
)


urlpatterns = [
    path("", home, name="home"),
    path("nuevo/", CrearPerfil.as_view(), name="crear_form"),
    path("listar/", ListarPerfil.as_view(), name="listar_perfiles"),
    path("editar/<int:id_perfil>/", editarPerfil, name="editar_perfil"),
    path("eliminar/<int:id_perfil>/", eliminarPerfil, name="eliminar_perfil"),
    path("administrador/", administrador, name="administrador"),
    path("acceso/", listaAcceso, name="lista_acceso"),
    path("<int:id_usuario>/", proyectos_usuario, name="proyectos_usuario"),
    path("administrador/<int:id_perfil>", concederAcceso, name="conceder_acceso"),
]
