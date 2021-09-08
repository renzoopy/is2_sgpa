from roles.models import Rol
from roles.forms import Rol_Form
from usuarios.models import Perfil
from miembros.models import Miembro
from django.urls.base import reverse
from proyectos.models import Proyecto
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission, User


# === Vista para la creación de un rol === #
class Crear_Rol(LoginRequiredMixin, CreateView):

    redirect_field_name = "redirect_to"
    model = Rol
    form_class = Rol_Form
    template_name = "roles/rol_form.html"

    def get_success_url(self):
        return reverse("roles:listar_roles.html", args=(self.kwargs["idProyecto"],))

    def get_form_kwargs(self, kwargs):
        form_kwargs = super(Crear_Rol, self).get_form_kwargs(kwargs)
        form_kwargs["idProyecto"] = self.kwargs["idProyecto"]
        return form_kwargs

    def form_valid(self, form):
        proyecto = Proyecto.objects.get(id=self.kwargs["idProyecto"])
        form.instance.proyecto = proyecto
        nombreRol = form.cleaneddata["nombre"]
        nombreGrupo = "{}{}".format(nombreRol, proyecto.id)
        grupo = Group.objects.create(name=nombreGrupo)
        form.instance.grupo = grupo
        permisos = Permission.objects.filter(name__in=form.cleaned_data["select"])
        grupo.permissions.set(permisos)
        return super(Crear_Rol, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Crear_Rol, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context


# === Vista para listar roles existentes === #
class Listar_Rol(LoginRequiredMixin, CreateView):

    redirect_field_name = "redirect_to"
    model = Rol
    template_name = "roles/listar_roles.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Listar_Rol, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context

    def get_queryset(self):
        return Rol.objects.filter(proyectos=self.kwargs["idPoryecto"]).order_by("id")


# === Vista para eliminar un rol === #
def ELiminar_Rol(request, idProyecto, id_rol):
    rol = Rol.objects.get(id=id_rol)
    if request.method == "POST":
        grupo = Group.objects.get(id=rol.grupo.id)
        grupo.delete()
        rol.delete()
        return redirect("roles:listar_roles", idProyecto=idProyecto)
    return render(
        request, "roles/eliminar_rol.html", {"rol": rol, "idProyecto": idProyecto}
    )


# === Vista para la edición de un rol === #
@login_required
def Editar_Rol(request, idProyecto, id_rol):
    rol = Rol.objects.get(id=id_rol)
    grupo = Group.objects.get(id=rol.grupo.id)
    if request.method == "GET":
        form = Rol_Form(instance=rol, idProyecto=idProyecto)
    else:
        form = Rol_Form(request.POST, instance=rol, idProyecto=idProyecto)
        if form.is_valid():
            permisos = Permission.objects.filter(name__in=form.cleaned_data["select"])
            grupo.permissions.set(permisos)
            form.save()
        return redirect("roles:listar_roles", idProyecto=idProyecto)
    return render(
        request, "roles/editar_rol.html", {"form": form, "idProyecto": idProyecto}
    )


# === Asignación de un rol === #
@login_required
def asignar_Rol(request, idProyecto, idMiembro, idRol):

    miembro = Miembro.objects.get(id=idMiembro)
    user = miembro.idPerfil.user
    rol = Rol.objects.get(id=idRol)
    rol.grupo.user_set.add(user)
    return redirect("miembros:ver_roles", idProyecto=idProyecto, idMiembro=idMiembro)


# === Revocar un rol === #
@login_required
def desasignar_Rol(request, idProyecto, idMiembro, idRol):

    miembro = Miembro.objects.get(id=idMiembro)
    user = miembro.idPerfil.user
    rol = Rol.objects.get(id=idRol)
    rol.grupo.user_set.remove(user)
    return redirect("miembros:ver_roles", idProyecto=idProyecto, idMiembro=idMiembro)


# === Ver todos los roles === #
@login_required
def verRoles(request, idProyecto, idMiembro):

    miembro = Miembro.objects.get(id=idMiembro)
    user = miembro.idPerfil.user
    list = []
    for x in user.groups.all():
        list.append(x.name)
    # print(list)
    for x in range(0, len(list)):
        n = list[x].split("")
        list[x] = n[0]
    roles_asignados = Rol.objects.distinct("nombre").filter(
        nombrein=list, proyecto=idProyecto
    )
    roles_sinasignar = (
        Rol.objects.distinct("nombre")
        .exclude(nombrein=list)
        .exclude(fase=None)
        .filter(proyecto=idProyecto)
    )
    return render(
        request,
        "miembros/verRoles.html",
        {
            "roles_a": roles_asignados,
            "roles_sa": roles_sinasignar,
            "idProyecto": idProyecto,
            "idMiembro": idMiembro,
        },
    )