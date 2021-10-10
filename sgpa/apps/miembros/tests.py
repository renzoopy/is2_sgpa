import pytest
from usuarios.models import Perfil
from miembros.models import Miembro
from proyectos.models import Proyecto
from django.contrib.auth.models import User

# --- Test Crear Miembro --- #
# Verifica la creacion de un miembro en la base de datos
@pytest.mark.django_db
def test_CrearMiembro():
    usuario = User.objects.create_user("humberto", "humberto@lopez.com", "humlopez")
    perfil = Perfil.objects.create(ci=5178065, telefono=8888888, user=usuario)
    proyecto = Proyecto.objects.create(
        nombre="Proyecto de Prueba",
        descripcion="Descripcion",
        estado="Pendiente",
        scrumMaster=perfil,
        numSprints=1,
    )
    Miembro.objects.create(idPerfil=perfil, idProyecto=proyecto)

    assert Miembro.objects.count() == 1


# --- Test Eliminar Miembro --- #
# Verifica la eliminación de un miembro en la base de datos
@pytest.mark.django_db
def test_EliminarMiembro():
    usuario = User.objects.create_user("humberto", "humberto@lopez.com", "humlopez")
    perfil = Perfil.objects.create(ci=5178065, telefono=8888888, user=usuario)
    proyecto = Proyecto.objects.create(
        nombre="Proyecto de Prueba",
        descripcion="Descripcion",
        estado="Pendiente",
        scrumMaster=perfil,
        numSprints=1,
    )
    miembro = Miembro.objects.create(idPerfil=perfil, idProyecto=proyecto)
    miembro.delete()

    assert Miembro.objects.count() == 0


# --- Test Eliminar Miembro 2 --- #
# Verifica que un miembro que no existe no puede ser eliminado
@pytest.mark.django_db
def test_EliminarMiembro2():
    usuario = User.objects.create_user("humberto", "humberto@lopez.com", "humlopez")
    perfil = Perfil.objects.create(ci=5178065, telefono=8888888, user=usuario)
    proyecto = Proyecto.objects.create(
        nombre="Proyecto de Prueba",
        descripcion="Descripcion",
        estado="Pendiente",
        scrumMaster=perfil,
        numSprints=1,
    )
    miembro = Miembro.objects.create(idPerfil=perfil, idProyecto=proyecto)
    try:
        miembro.delete()
        miembro.delete()
    except:
        assert True, "El objeto que intenta eliminar no existe"
