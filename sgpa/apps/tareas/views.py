from django.http.response import HttpResponseRedirect
from usuarios.models import Perfil
from django.shortcuts import redirect, render
from tareas.models import UserStory
from django.urls.base import reverse
from tareas.forms import UserStoryForm
from django.contrib.auth.models import User
from proyectos.models import Backlog, Historial, Proyecto
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# --- Crear User Story --- #
class CrearUserStory(LoginRequiredMixin, CreateView):
    """
    Vista basada en modelos que permite crear un User Story con los campos correspondientes
    No recibe parámetros
    Requiere inicio de sesión
    """

    redirect_field_name = "redirect_to"
    model = UserStory
    form_class = UserStoryForm
    template_name = "tareas/nuevo_userStory.html"

    def get_success_url(self):
        return reverse("tareas:listar_tareas", args=(self.kwargs["idProyecto"],))

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(CrearUserStory, self).get_form_kwargs(**kwargs)
        form_kwargs["idProyecto"] = self.kwargs["idProyecto"]
        return form_kwargs

    def form_valid(self, form):
        proyecto = Proyecto.objects.get(id=self.kwargs["idProyecto"])
        form.instance.proyecto = proyecto
        backlog = Backlog.objects.get(proyecto=proyecto, tipo="Product_Backlog")
        backlog.numTareas += 1
        user = User.objects.get(username=self.request.user)
        perfil = Perfil.objects.get(user=user)
        Historial.objects.create(
            operacion="Crear User Story {}".format(form.instance.nombre),
            autor=perfil.__str__(),
            proyecto=proyecto,
            categoria="User Story",
        )
        return super(CrearUserStory, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearUserStory, self).get_context_data(**kwargs)
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context


# --- Listar User Story --- #
class ListarUserStory(LoginRequiredMixin, ListView):
    """
    Vista basada en modelos que permite listar todos los user stories creados
    Muestra la lista de los user stories asociados al proyecto en forma de tabla
    No recibe parámetros
    Requiere inicio de sesión
    """

    redirect_field_name = "redirect_to"
    model = UserStory
    template_name = "tareas/listar_userStory.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ListarUserStory, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context

    def get_queryset(self):
        proyecto = Proyecto.objects.get(id=self.kwargs["idProyecto"])
        backlog = Backlog.objects.get(proyecto=proyecto)
        return UserStory.objects.filter(backlog=backlog)


def crearUserStori(request, idProyecto):
    proyecto = Proyecto.objects.get(id=idProyecto)
    data = {"idProyecto": idProyecto}

    if request.method == "GET":
        data["form"] = UserStoryForm()
        return render(request, "tareas/nuevo_userStory.html", data)

    elif request.method == "POST":
        form = UserStoryForm(request.POST)

        if form.is_valid():
            print("HASTA ACA LLEGA")
            backlog = Backlog.objects.get(proyecto=proyecto, tipo="Product_Backlog")
            backlog.numTareas += 1
            backlog.save()
            proyecto.save()
            print("CREAR USER STORY")
            userStory = UserStory.objects.create(
                backlog=backlog,
                nombre=form.cleaned_data["nombre"],
                descripcion=form.cleaned_data["descripcion"],
                prioridad=form.cleaned_data["prioridad"],
            )
            print("USER STORY CREADO")
            userStory.save()
            print("US SAVE")

            # return HttpResponseRedirect(
            #     reverse("tareas:listar_tareas", kwargs={"idProyecto": idProyecto})
            # )
            return redirect("tareas:listar_tareas", idProyecto)
        print("NO RETORNA")

        data["form"] = form
        return render(request, "tareas/nuevo_userStory.html", data)
