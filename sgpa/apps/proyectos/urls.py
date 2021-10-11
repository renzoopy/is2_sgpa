from os import name
from django.contrib import admin
from django.urls import path, include
from proyectos.views import (
    finalizarProyecto,
    home,
    verProyecto,
    crearProyecto,
    iniciarProyecto,
    cancelarProyecto,
    listarProyectos,
    eliminarProyecto,
    modificarProyecto,
    proy,
    crearSprints,
    listarSprint,
)

urlpatterns = [
    path("", proy, name="proy"),
    path("home/", home, name="home"),
    path("nuevo/", crearProyecto.as_view(), name="nuevo_proyecto"),
    path("listar/", listarProyectos.as_view(), name="listar_proyectos"),
    path("eliminar/<int:id_proyecto>/", eliminarProyecto, name="eliminar_proyectos"),
    path("<int:id_proyecto>/", verProyecto, name="ver_proyecto"),
    path("modificar/<int:id_proyecto>/", modificarProyecto, name="modificar_proyecto"),
    path("<int:id_proyecto>/iniciar/", iniciarProyecto, name="iniciar_proyecto"),
    path("<int:id_proyecto>/finalizar/", finalizarProyecto, name="finalizar_proyecto"),
    path("<int:id_proyecto>/cancelar/", cancelarProyecto, name="cancelar_proyecto"),
    path(
        "<int:id_proyecto>/listarSprints/",
        listarSprint.as_view(),
        name="listar_sprints",
    ),
    path("sprint/nuevo/", crearSprints.as_view(), name="nuevo_sprint"),
]
