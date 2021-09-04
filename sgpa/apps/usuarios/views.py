from django.http import request
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
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

    # def get_context_data(self, **kwargs):
    #     context = super(CrearPerfil, self).get_context_data(**kwargs)
    #     perfil = Perfil.objects.get(user=self.request.user)
    #     print(perfil)
    #     return context

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


class ListarPerfil(LoginRequiredMixin, ListView):

    redirect_field_name = "redirect_to"
    model = Perfil
    template_name = "usuarios/listar_perfiles.html"


# @login_required
# def eliminarPerfil(request, id_perfil):

#     perfil = Perfil.objects.get(id=id_perfil)
