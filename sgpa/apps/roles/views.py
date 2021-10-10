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


# --- Vista para la creación de un rol --- #
class CrearRol(LoginRequiredMixin, CreateView):

    redirect_field_name = "redirect_to"
    model = Rol
    form_class = Rol_Form
    template_name = "roles/nuevo_rol.html"

    def get_success_url(self):
        return reverse("roles:listar_roles", args=(self.kwargs["idProyecto"],))

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(CrearRol, self).get_form_kwargs(**kwargs)
        form_kwargs["idProyecto"] = self.kwargs["idProyecto"]
        return form_kwargs

    def form_valid(self, form):
        proyecto = Proyecto.objects.get(id=self.kwargs["idProyecto"])
        form.instance.proyecto = proyecto
        nombreRol = form.cleaned_data["nombre"]
        nombreGrupo = "{}{}".format(nombreRol, proyecto.id)
        grupo = Group.objects.create(name=nombreGrupo)
        form.instance.grupo = grupo
        permisos = Permission.objects.filter(name__in=form.cleaned_data["select"])
        grupo.permissions.set(permisos)
        return super(CrearRol, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearRol, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context


# --- Vista para listar roles existentes --- #
class ListarRol(LoginRequiredMixin, ListView):

    redirect_field_name = "redirect_to"
    model = Rol
    template_name = "roles/listar_roles.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ListarRol, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context

    def get_queryset(self):
        return Rol.objects.filter(proyecto=self.kwargs["idProyecto"]).order_by("id")


# --- Vista para eliminar un rol --- #
def eliminarRol(request, idProyecto, id_rol):
    rol = Rol.objects.get(id=id_rol)
    if request.method == "POST":
        grupo = Group.objects.get(id=rol.grupo.id)
        grupo.delete()
        rol.delete()
        return redirect("roles:listar_roles", idProyecto=idProyecto)
    return render(
        request, "roles/eliminar_rol.html", {"rol": rol, "idProyecto": idProyecto}
    )


# --- Vista para la edición de un rol --- #
@login_required
def editarRol(request, idProyecto, id_rol):
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


# --- Asignación de un rol --- #
@login_required
def asignarRol(request, idProyecto, idMiembro, idRol):
    miembro = Miembro.objects.get(id=idMiembro)
    user = User.objects.get(id=idMiembro)
    rol = Rol.objects.get(id=idRol)
    rol.grupo.user_set.add(user)
    return redirect("miembros:ver_roles", idProyecto=idProyecto, idMiembro=idMiembro)


# --- Revocar un rol --- #
@login_required
def desasignarRol(request, idProyecto, idMiembro, idRol):

    miembro = Miembro.objects.get(id=idMiembro)
    user = User.objects.get(id=idMiembro)
    rol = Rol.objects.get(id=idRol)
    rol.grupo.user_set.remove(user)
    return redirect("miembros:ver_roles", idProyecto=idProyecto, idMiembro=idMiembro)


# --- Ver todos los roles --- #
@login_required
def verRoles(request, idProyecto, idMiembro):
    roles = Rol.objects.filter(proyecto=idProyecto)
    user = User.objects.get(id=idMiembro)
    roles_asignados = []
    roles_noasignados = []

    for x in roles:
        roles_noasignados.append(x)

    for i in user.groups.filter(user=idMiembro):
        for x in roles:
            if i.name.startswith(x.nombre):
                roles_asignados.append(x)

    diferencia = set(roles_noasignados) - set(roles_asignados)
    roles_noasignados = list(diferencia)
    return render(
        request,
        "miembros/ver_roles.html",
        {
            "roles_a": roles_asignados,
            "roles_sa": roles_noasignados,
            "idProyecto": idProyecto,
            "idMiembro": idMiembro,
        },
    )
