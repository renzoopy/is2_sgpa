from usuarios.models import Perfil
from miembros.models import Miembro
from proyectos.models import Proyecto
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import redirect, render
from proyectos.forms import ProyectoAdminForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def base(request):
    return render(request, "base.html")


def proy(request):
    return render(request, "sprints/sprint.html")


def home(request):
    return render(request, "home.html")


class crearProyecto(LoginRequiredMixin, ListView):
    redirect_field_name = "redirect_to"
    model = Proyecto
    form_class = ProyectoAdminForm
    template_name = "proyectos/nuevoProyecto.html"

    def get_success_url(self):
        scrummaster = Perfil.objects.get(id=self.request.POST["srummaster"])
        proyecto = Proyecto.objects.get(id=self.object.pk)
        Miembro.objects.create(idPerfil=scrummaster, idProyecto=proyecto)
        equipo = Group.objects.create(name="equipo%s" % self.object.pk)
        proyecto.equipo = equipo
        proyecto.save()
        return reverse_lazy("usuarios:administrador")


class listarProyectos(LoginRequiredMixin, ListView):
    redirect_field_name = "redirect_to"
    model = Proyecto
    template_name = "proyectos/listarProyectos.html"
    ordering = ["id"]
