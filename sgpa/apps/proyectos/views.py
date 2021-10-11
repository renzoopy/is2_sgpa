from datetime import datetime
from django.http import request
from usuarios.models import Perfil
from django.contrib import messages
from miembros.models import Miembro
from tareas.models import UserStory
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from proyectos.models import Proyecto, Sprint
from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from proyectos.forms import Proyecto_Form, ProyectoEdit_Form, Sprint_Form
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required


def base(request):
    return render(request, "base.html")


def proy(request):
    if request.user.is_authenticated:
        return render(request, "sprints/sprint.html")
    else:
        return redirect("login")


def home(request):
    return render(request, "home.html")


# --- Crear Proyecto --- #
class crearProyecto(LoginRequiredMixin, CreateView):
    model = Proyecto
    redirect_field_name = "redirect_to"
    form_class = Proyecto_Form
    template_name = "proyectos/nuevo_proyecto.html"

    def get_success_url(self):
        proyecto = Proyecto.objects.get(id=self.object.pk)
        scrummaster = Perfil.objects.get(id=self.request.POST.get("scrumMaster"))
        Miembro.objects.create(idPerfil=scrummaster, idProyecto=proyecto)
        equipo = Group.objects.create(name="equipo%s" % self.object.pk)
        proyecto.equipo = equipo
        proyecto.save()

        return reverse_lazy("usuarios:administrador")


# --- Listar Proyectos --- #
class listarProyectos(LoginRequiredMixin, ListView):
    model = Proyecto
    redirect_field_name = "redirect_to"
    template_name = "proyectos/listar_proyectos.html"
    ordering = ["id"]


# --- Eliminar Proyecto --- #
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


# --- Ver Proyecto --- #
@login_required
def verProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    sprints = Sprint.objects.filter(proyecto=id_proyecto)
    miembros = Miembro.objects.filter(idProyecto=id_proyecto)
    return render(
        request,
        "proyectos/ver_proyecto.html",
        {"miembros": miembros, "proyecto": proyecto, "sprints": sprints},
    )


# --- Modificar Proyecto --- #
@login_required
def modificarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)

    if request.method == "GET":
        proyecto_Form = ProyectoEdit_Form(instance=proyecto)
    else:
        proyecto_Form = ProyectoEdit_Form(request.POST, instance=proyecto)
        if proyecto_Form.is_valid():
            proyecto_Form.save()
        return redirect("proyectos:ver_proyecto", id_proyecto)
    return render(
        request,
        "proyectos/modificar_proyecto.html",
        {"proyecto_Form": proyecto_Form, "id_proyecto": id_proyecto},
    )


# --- Iniciar Proyecto --- #
@login_required
def iniciarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    sprints = Sprint.objects.filter(proyecto=id_proyecto)
    contador = 0
    if len(sprints) == proyecto.numSprints:
        contador += 1
        print("Existen Sprints xD")
    else:
        messages.add_message(
            request, messages.ERROR, "El sprint planning aún no fue realizado"
        )
        messages.error(request, "El sprint planning aún no fue realizado")

    if len(sprints) > 0:
        for tareas in range(0, len(sprints)):
            if len(UserStory.objects.filter(sprint=sprints[tareas])) > 0:
                contador += 1
                print("Encontró US")
            else:
                print("No se encontraron US")
                messages.add_message(
                    request,
                    messages.ERROR,
                    "No se encontraron Historias de Usuario para este sprint",
                )
    print("Contador es igual a = ", contador)
    contador += 1
    if contador == 2:
        proyecto.estado = "Iniciado"
        proyecto.fechaInicio = datetime.now()
        proyecto.save()
    return redirect("proyectos:ver_proyecto", id_proyecto)


# --- Cancelar Proyecto --- #
@login_required
def cancelarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    sprints = Sprint.objects.filter(proyecto=id_proyecto)
    for sprint in sprints:
        sprint.estado = "Cancelado"
        sprint.save()
    proyecto.estado = "Cancelado"
    proyecto.fechaFin = datetime.now()
    proyecto.save()
    return redirect("proyectos:ver_proyecto", id_proyecto)


# --- Finalizar Proyecto --- #
@login_required()
def finalizarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id=id_proyecto)
    sprints = Sprint.objects.filter(proyecto=id_proyecto)
    i = len(sprints)
    for iterador in range(0, len(sprints)):
        if sprints[iterador].estado != "Finalizado":
            messages.add_message(request, messages.ERROR, "Sprint sin finalizar")
            i -= 1
    if i == len(sprints):
        proyecto.estado = "Finalizado"
        proyecto.fechaFin = datetime.now()
        proyecto.save()
    return redirect("proyectos:ver_proyecto", id_proyecto)


# --- Crear Sprint --- #
@login_required()
def crearSprint(request, id_proyecto):
    form = Sprint_Form(request.POST or None)
    form.initial["proyecto"] = id_proyecto
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    datos = {"proyecto": proyecto, "form": form, "title": "Crear Sprint"}
    if form.is_valid():
        if (
            form.cleaned_data["fecha_inicio"] != None
            and form.cleaned_data["fecha_fin"] != None
        ):
            ini = (form.cleaned_data["fecha_inicio"]).date()
            fin = (form.cleaned_data["fecha_fin"]).date()
            aux = (fin - ini).days
            if aux >= 0:
                sprint = form.save()
            else:
                datos["Error_fechas"] = True
                template = "sprint/crear_sprint.html"
                return render(request, template, datos)
        else:
            sprint = form.save()

    if request.method == "POST":
        return redirect(reverse("sprint", kwargs={"proyecto_id": proyecto.id}))
    else:
        template = "sprint/crear_sprint.html"
        return render(request, template, datos)


# --- Crear Sprint 2--- #
class crearSprints(LoginRequiredMixin, CreateView):
    model = Sprint
    redirect_field_name = "redirect_to"
    form_class = Sprint_Form
    template_name = "sprints/nuevo_sprint.html"

    def get_success_url(self):
        return reverse_lazy(
            "proyectos:listar_sprints", args=(self.kwargs["idroyecto"],)
        )

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(crearSprints, self).get_form_kwargs(**kwargs)
        form_kwargs["idProyecto"] = self.kwargs["idProyecto"]
        return form_kwargs

    def form_valid(self, form):
        proyecto = Proyecto.objects.get(id="idProyecto")
        sprint = Sprint.objects.get(id=self.object.pk)
        sprint.proyecto = proyecto
        sprint.save()
        return super(crearSprints, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(crearSprints, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context


# --- Ver Sprints --- #
class listarSprint(LoginRequiredMixin, ListView):
    model = Sprint
    redirect_field_name = "redirect_to"
    template_name = "sprints/listar_sprints.html"
    ordering = ["id"]
