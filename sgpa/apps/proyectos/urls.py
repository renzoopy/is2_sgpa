from os import name
from django.contrib import admin
from django.urls import path, include

from proyectos.views import (
    crearProyecto,
    home,
    listarProyectos,
    proy,
    eliminarProyecto,
    verProyecto,
    modificarProyecto,
)

urlpatterns = [
    path("", proy, name="proy"),
    path("home/", home, name="home"),
    path("nuevo/", crearProyecto.as_view(), name="nuevo_proyecto"),
    path("listar/", listarProyectos.as_view(), name="listar_proyectos"),
    path("eliminar/<int:id_proyecto>/", eliminarProyecto, name="eliminar_proyectos"),
    path("<int:id_proyecto>/", verProyecto, name="ver_proyecto"),
    path("modificar/<int:id_proyecto>/", modificarProyecto, name="modificar_proyecto"),
]
