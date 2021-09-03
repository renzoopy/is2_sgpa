from django.urls import path, include
from roles.views import CrearRol, ListarRol

urlpatterns = [
    path("nuevo/", CrearRol.as_view(), name="crear_rol"),
    path("listar/", ListarRol.as_view(), name="listar_roles"),
]
