from django.urls import path, include
from roles.views import Crear_Rol, ELiminar_Rol, Editar_Rol, Listar_Rol

urlpatterns = [
    path("nuevo/", Crear_Rol.as_view(), name="crear_rol"),
    path("listar/", Listar_Rol.as_view(), name="listar_roles"),
    path("eliminar/<int:id_rol>/", ELiminar_Rol, name="eliminar_rol"),
    path("editar/<int:id_rol>/", Editar_Rol, name="editar_rol"),
]