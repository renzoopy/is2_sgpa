from usuarios.models import Perfil
from miembros.models import Miembro
from proyectos.models import Proyecto
from miembros.forms import MiembrosForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# --- Crear nuevo Miembro --- #
@login_required
def miembroCrear(request, idProyecto):

    if request.method == "POST":
        form = MiembrosForm(request.POST, idProyecto=idProyecto)

        if form.is_valid():
            miembro = form.save(commit=False)
            miembro.idProyecto = Proyecto.objects.get(id=idProyecto)
            miembro.save()

        return redirect("miembros:listar", idProyecto=idProyecto)

    else:
        form = MiembrosForm(request.POST or None, idProyecto=idProyecto)

    return render(
        request, "miembros/nuevo_miembro.html", {"form": form, "idProyecto": idProyecto}
    )


# --- Eliminar Miembro --- #
@login_required
def miembroEliminar(request, idProyecto, idMiembro):
    miembro = Miembro.objects.get(idPerfil=idMiembro, idProyecto=idProyecto)
    if request.method == "POST":
        miembro.delete()

        return redirect("miembros:listar", idProyecto=idProyecto)
    return render(
        request,
        "miembros/eliminar_miembro.html",
        {"miembros": miembro, "idProyecto": idProyecto},
    )


# --- Listar Miembros --- #
@login_required
def verMiembros(request, idProyecto):

    miembros = Miembro.objects.filter(idProyecto=idProyecto)

    return render(
        request,
        "miembros/ver_miembros.html",
        {
            "miembros": miembros,
            "idProyecto": idProyecto,
        },
    )
