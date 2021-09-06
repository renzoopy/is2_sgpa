from django.urls import path, include
from roles.views import CrearRol, ELiminarRol, EditarRol, ListarRol

urlpatterns = [
    path("nuevo/", CrearRol.as_view(), name="crear_rol"),
    path("listar/", ListarRol.as_view(), name="listar_roles"),
    path("eliminar/<int:id_rol>/", ELiminarRol, name="eliminar_rol"),
    path("editar/<int:id_rol>/", EditarRol, name="editar_rol"),
]
