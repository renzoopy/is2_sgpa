from usuarios.models import Perfil
from proyectos.models import Proyecto
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.models import Group, User
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


class ProyectoCrear(LoginRequiredMixin, ListView):
    redirect_field_name = "redirect_to"
    model = Proyecto
    form_class = ProyectoAdminForm
    template_name = "proyectos/nuevoProyecto.html"

    def get_success_url(self):
        scrummaster = Perfil.objects.get(id=self.request.POST["srummaster"])
        proyecto = Proyecto.objects.get(id=self.object.pk)
        equipo = Group.objects.create(name="comite%s" % self.object.pk)
        proyecto.equipo = equipo
        proyecto.save()
        return reverse_lazy("proyectos:sprint")


class ProyectoListar(LoginRequiredMixin, ListView):
    redirect_field_name = "redirect_to"
    model = Proyecto
    template_name = "proyectos/listarProyectos.html"
    ordering = ["id"]
