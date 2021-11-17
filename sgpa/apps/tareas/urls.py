from django.urls import path, include
from tareas.views import ListarUserStory, CrearUserStory, crearUserStori

urlpatterns = [
    path("nuevo/", crearUserStori, name="crear_tarea"),
    path("listar/", ListarUserStory.as_view(), name="listar_tareas"),
]
