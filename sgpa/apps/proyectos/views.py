from usuarios.models import Perfil
from proyectos.models import Proyecto
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from proyectos.forms import ProyectoAdminForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def base(request):
    return render(request, "base.html")


def proy(request):
    return render(request, "sprints/sprint.html")


def home(request):
    return render(request, "home.html")


def nuevoProyecto(request):
    return render(request, "proyectos/nuevoProyecto.html")


class ProyectoCrear(LoginRequiredMixin, ListView):
    redirect_field_name = "redirect_to"
    model = Proyecto
    form_class = ProyectoAdminForm
    template_name = "nuevoProyecto.html"

    def get_success_url(self):
        scrummaster = Perfil.objects.get(id=self.request.POST["srummaster"])
        proyecto = Proyecto.objects.get(id=self.object.pk)
        proyecto.save()
        return reverse_lazy("proyectos:sprint")


class ProyectoListar(LoginRequiredMixin, ListView):
    redirect_field_name = "redirect_to"
    model = Proyecto
    template_name = "proyectos/listarProyectos.html"
    ordering = ["id"]
