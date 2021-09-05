from usuarios.models import Perfil
from miembros.models import Miembro
from proyectos.models import Proyecto
from miembros.forms import MiembrosForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

# === Crear nuevo Miembro === #
@login_required
def miembroCrear(request, idProyecto):

    if request.method == "POST":
        form = MiembrosForm(request.POST, idProyecto=idProyecto)

        if form.is_valid():
            miembro = form.save(commit=False)
            miembro.idProyecto = Proyecto.objects.get(id=idProyecto)
            miembro.save()
            user = User.objects.get(username=request.user)
            perfil = Perfil.objects.get(user=user)

        return redirect("miembros:lista", idProyecto=idProyecto)

    else:
        form = MiembrosForm(request.POST or None, idProyecto=idProyecto)

    return render(
        request, "miembros/nuevoMiembro.html", {"form": form, "proyecto": idProyecto}
    )


# === Eliminar Miembro === #
@login_required
def miembroEliminar(request, idProyecto, idMiembro):

    miembro = Miembro.objects.get(id=idMiembro)
    if request.method == "POST":
        miembro.delete()
        user = User.objects.get(username=request.user)
        perfil = Perfil.objects.get(user=user)

        return redirect("miembros:lista", idProyecto=idProyecto)
    return render(
        request,
        "miembros/eliminarMiembro.html",
        {"miembros": miembro, "idProyecto": idProyecto},
    )


# === Listar Miembros === #
@login_required
def verMiembros(request, idProyecto):

    proyecto = Proyecto.objects.get(id=idProyecto)
    miembro = proyecto.miembro_set.all()
    perfil = Perfil.objects.all()
    valid_id = []
    for p in perfil:
        if not Miembro.objects.filter(idProyecto=proyecto).filter(idPerfil=p).exists():
            if not p.id == 1:
                valid_id.append(p.id)
    perfiles = Perfil.objects.filter(id__in=valid_id)
    miembro = Miembro.objects.filter(idProyecto=idProyecto)
    g = proyecto.gerente
    return render(
        request,
        "miembros/verMiembros.html",
        {
            "miembros": miembro,
            "gerente": g,
            "idProyecto": idProyecto,
            "participantes_para_agregar": perfiles.all().count() > 0,
        },
    )
