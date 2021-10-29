from django.urls import path, include
from tareas.views import ListarUserStory, CrearUserStory

urlpatterns = [
    path("nuevo/", CrearUserStory.as_view(), name="crear_tarea"),
    path("listar/", ListarUserStory.as_view(), name="listar_tareas"),
]
