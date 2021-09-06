from django.db.models import Q
from django.http import request
from usuarios.models import Perfil
from django.contrib import messages
from miembros.models import Miembro
from django.urls import reverse_lazy
from proyectos.models import Proyecto
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from usuarios.forms import Perfil_Form, Usuario_Form
from django.contrib.auth.models import User, Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    return render(request, "home.html")


# === Creación de Perfil === #
class CrearPerfil(LoginRequiredMixin, CreateView):
    model = Perfil
    form_class = Perfil_Form
    template_name = "usuarios/perfil_form.html"
    success_url = reverse_lazy("usuarios:home")

    def form_valid(self, form):
        user = User.objects.get(username=self.request.user)
        Perfil.objects.create(
            user=user,
            ci=self.request.POST["ci"],
            telefono=self.request.POST["telefono"],
        )
        return redirect(self.success_url)


# === Editar Perfil === #
@login_required
def editarPerfil(request, id_perfil):

    perfil = Perfil.objects.get(id=id_perfil)
    usuario = User.objects.get(id=perfil.user.id)
    if request.method == "GET":
        perfil_Form = Perfil_Form(instance=perfil)
        usuario_Form = Usuario_Form(instance=usuario)
    else:
        perfil_Form = Perfil_Form(request.POST, instance=perfil)
        usuario_Form = Usuario_Form(request.POST, instance=usuario)
        if all([perfil_Form.is_valid(), usuario_Form.is_valid()]):
            perfil_Form.save()
            usuario_Form.save()
        return redirect("usuarios:listar_perfiles")
    return render(
        request,
        "usuarios/editar_perfil.html",
        {"perfil_Form": perfil_Form, "usuario_Form": usuario_Form},
    )


# === Listar Perfiles === #
class ListarPerfil(LoginRequiredMixin, ListView):

    redirect_field_name = "redirect_to"
    model = Perfil
    template_name = "usuarios/listar_perfiles.html"


# === Eliminar Perfil === #
@login_required
def eliminarPerfil(request, id_perfil):

    perfil = Perfil.objects.get(id=id_perfil)
    miembro = Miembro.objects.filter(idPerfil=perfil.id)
    if not miembro:
        if request.method == "POST":
            usuario = User.objects.get(id=perfil.user.id)
            usuario.delete()
            perfil.delete()
            return redirect("usuarios:listar_perfiles")
        return render(request, "usuarios/eliminar_perfil.html", {"perfil": perfil})
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "No se puede eliminar al usuario: %s  porque forma parte de un proyecto"
            % perfil.user.first_name,
        )
        return redirect("usuarios:listar_perfiles")


# === Apartado Administrador === #


@login_required
@permission_required("usuarios.autorizar_usuario", login_url="usuarios:home")
def administrador(request):

    proyectos = Proyecto.objects.all()
    permiso = Permission.objects.get(codename="acceso_usuario")
    usuario = User.objects.filter(~Q(user_permissions=permiso), ~Q(id=1))
    perfilesAcceso = Perfil.objects.none()
    if len(usuario) > 0:
        perfilesAcceso = Perfil.objects.filter(Q(user=usuario[0]))
        for x in range(1, len(usuario)):
            perfilesAcceso |= Perfil.objects.filter(Q(user=usuario[x]))
    return render(
        request,
        "usuarios/administrador.html",
        {"perfilesAcceso": perfilesAcceso, "proyectos": proyectos},
    )


# === Listar Solicitudes de Acceso === #
@login_required
@permission_required("usuarios.autorizar_usuario", login_url="usuarios:home")
def listaAcceso(request):

    perm = Permission.objects.get(codename="acceso_usuario")
    usuario = User.objects.filter(~Q(user_permissions=perm))
    perfiles = Perfil.objects.filter(Q(user=usuario[0]))
    for x in range(1, len(usuario)):
        perfiles |= Perfil.objects.filter(Q(user=usuario[x]))
    contexto = {"perfiles": perfiles}
    return render(request, "usuarios/usuario_acceso.html", contexto)


# === Conceder Acceso al Sistema === #
@login_required
@permission_required("usuarios.autorizar_usuario", login_url="usuarios:home")
def concederAcceso(request, id_perfil):

    perfil = Perfil.objects.get(id=id_perfil)
    usuario = User.objects.get(id=perfil.user.id)
    perm = Permission.objects.get(codename="acceso_usuario")
    usuario.user_permissions.add(perm)
    send_mail(
        "Solicitud de acceso a SGPA",
        "¡Bienvenido a SGPA! Su solicitud de acceso al sistema fue aceptada",
        settings.EMAIL_HOST_USER,
        [usuario.email],
    )
    return redirect("usuarios:administrador")


# === Proyectos de Usuario === #
@login_required
def proyectos_usuario(request, id_usuario):

    usuario = User.objects.get(id=id_usuario)
    perfil = Perfil.objects.get(user=usuario)
    miembro = Miembro.objects.filter(idPerfil=perfil.id)
    return render(request, "usuarios/proyectos.html", {"miembros": miembro})
