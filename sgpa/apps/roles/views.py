from django.contrib.auth.models import Group, Permission, User
from proyectos.models import Proyecto
from roles.models import Rol
from roles.forms import Rol_Form
from django.urls.base import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

# Create your views here.


class CrearRol(LoginRequiredMixin, CreateView):

    redirect_field_name = "redirect_to"
    model = Rol
    form_class = Rol_Form
    template_name = "roles/roles_form.html"

    def get_success_url(self):
        return reverse("roles:listar_roles.html", args=(self.kwargs["idProyecto"],))

    def get_form_kwargs(self, **kwargs):
        form_kwargs = super(CrearRol, self).get_form_kwargs(**kwargs)
        form_kwargs["idProyecto"] = self.kwargs["idProyecto"]
        return form_kwargs

    def form_valid(self, form):
        proyecto = Proyecto.objects.get(id=self.kwargs["idProyecto"])
        form.instance.proyecto = proyecto
        nombreRol = form.cleaned_data["nombre"]
        nombreGrupo = "{}_{}".format(nombreRol, proyecto.id)
        grupo = Group.objects.create(name=nombreGrupo)
        form.instance.grupo = grupo
        permisos = Permission.objects.filter(name__in=form.cleaned_data["select"])
        grupo.permissions.set(permisos)
        return super(CrearRol, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearRol, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context


class ListarRol(LoginRequiredMixin, CreateView):

    redirect_field_name = "redirect_to"
    model = Rol
    template_name = "roles/listar_roles.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ListarRol, self).get_context_data()
        context["idProyecto"] = self.kwargs["idProyecto"]
        return context

    def get_queryset(self):
        return Rol.objects.filter(proyectos=self.kwargs["idPoryecto"]).order_by("id")
