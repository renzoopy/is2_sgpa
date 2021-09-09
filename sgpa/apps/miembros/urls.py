from django.urls import path
from roles.views import ver_Roles, asignar_Rol, desasignar_Rol
from miembros.views import miembroCrear, miembroEliminar, verMiembros


urlpatterns = [
    path("listar/", verMiembros, name="lista"),
    path("nuevo/", miembroCrear, name="nuevo"),
    path("<int:idMiembro>/eliminar/", miembroEliminar, name="eliminar"),
    path("<int:idMiembro>/roles/", ver_Roles, name="ver_roles"),
    path("<int:idMiembro>/roles/<int:idRol>/asignar/", asignar_Rol, name="asignar_rol"),
    path(
        "<int:idMiembro>/roles/<int:idRol>/desasignar/",
        desasignar_Rol,
        name="desasignar_rol",
    ),
]
