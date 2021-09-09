from usuarios.models import Perfil
from django.contrib import messages
from miembros.models import Miembro
from proyectos.models import Proyecto, Sprint
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from proyectos.forms import Proyecto_Form
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def base(request):
    return render(request, "base.html")


def proy(request):
    if request.user.is_authenticated:
        return render(request, "sprints/sprint.html")
    else:
        return redirect("login")


def home(request):
    return render(request, "home.html")


class crearProyecto(LoginRequiredMixin, CreateView):
    model = Proyecto
    redirect_field_name = "redirect_to"
    form_class = Proyecto_Form
    template_name = "proyectos/nuevoProyecto.html"

    def get_success_url(self):
        proyecto = Proyecto.objects.get(id=self.object.pk)
        scrummaster = Perfil.objects.get(id=self.request.POST.get("scrumMaster"))
        Miembro.objects.create(idPerfil=scrummaster, idProyecto=proyecto)
        equipo = Group.objects.create(name="equipo%s" % self.object.pk)
        proyecto.equipo = equipo
        proyecto.save()
        return reverse_lazy("usuarios:administrador")


class listarProyectos(LoginRequiredMixin, ListView):
    model = Proyecto
    redirect_field_name = "redirect_to"
    template_name = "proyectos/listarProyectos.html"
    ordering = ["id"]


@login_required
def eliminarProyecto(request, id_proyecto):

    proyecto = Proyecto.objects.get(id=id_proyecto)
    if proyecto.numSprints == 0:
        if request.method == "POST":
            proyecto.delete()
            return redirect("proyectos:listar_proyectos")
        return render(
            request,
            "proyectos/eliminar_proyecto.html",
            {"proyecto": proyecto},
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "No se puede eliminar el proyecto: existen %s sprints activos"
            % proyecto.numSprints,
        )
        return redirect("proyectos:listar_proyectos")
