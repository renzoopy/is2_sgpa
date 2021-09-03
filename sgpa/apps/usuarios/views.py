from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.models import Perfil
from usuarios.forms import Perfil_Form, Usuario_Form


def home(request):
    return render(request, "home.html")


# Creación de Perfil
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


#  Editar Perfil
@login_required
def editarPerfil(request, id_perfil):
    """
    Vista para editar la información de un usuario (el email no puede ser modificado)
    Recibe el request HTTP y el id del perfil de usuario
    Retorna la renderización de la información del usuario en el template especificado
    Requiere inicio de sesión
    """
    perfil = Perfil.objects.get(id=id_perfil)
    usuario = User.objects.get(id=perfil.user.id)
    if request.method == "GET":
        P_form = Perfil_Form(instance=perfil)
        U_form = Usuario_Form(instance=usuario)
    else:
        P_form = Perfil_Form(request.POST, instance=perfil)
        U_form = Usuario_Form(request.POST, instance=usuario)
        if all([P_form.is_valid(), U_form.is_valid()]):
            P_form.save()
            U_form.save()
        return redirect("usuarios:home")
    return render(
        request, "usuarios/editar_perfil.html", {"P_form": P_form, "U_form": U_form}
    )
