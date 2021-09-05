from django.urls import path
from miembros.views import miembroCrear, miembroEliminar, verMiembros


urlpatterns = [
    path("lista/", verMiembros, name="lista"),
    path("nuevo/", miembroCrear, name="nuevo"),
    path("<int:idMiembro>/eliminar/", miembroEliminar, name="eliminar"),
]
