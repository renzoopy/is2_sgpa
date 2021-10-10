from django.shortcuts import render
from tareas.models import UserStory
from proyectos.models import Proyecto, Sprint
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# --- Crear User Story --- #
@login_required
def CrearTarea(request, idProyecto, idSprint, idTipo):
    sprint = Sprint.objects.get(id=idSprint)


# --- Listar User Story --- #
