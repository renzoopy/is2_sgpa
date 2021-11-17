from django import forms
from django.forms import Form, CharField, IntegerField
from tareas.models import UserStory
from proyectos.models import Proyecto


class UserStoryForm(Form):
    nombre = CharField()
    descripcion = CharField()
    prioridad = IntegerField()
    # def __init__(self, *args, **kwargs):
    #     id = kwargs.pop("idProyecto")
    #     super(UserStoryForm, self).__init__(*args, **kwargs)
    #     proyecto = Proyecto.objects.get(id=id)

    # class Meta:
    #     model = UserStory
    #     fields = ["nombre", "nombre"]
    #     labels = {"nombre": "Nombre", "descripcion": "descripcion"}
    #     widgets = {
    #         "nombre": forms.TextInput(attrs={"class": "form-control"}),
    #         "descripcion": forms.TextInput(attrs={"class": "form-control"}),
    #     }

    # def save(self, commit=True, *args, **kwargs):
    #     sprint = kwargs.get("sprint")
    #     nombre = kwargs.get("nombre")
    #     desarrollador = kwargs.get("desarrollador")
    #     descripcion = kwargs.get("descripcion")
    #     instance = super(UserStoryForm, self).save(commit=False)
    #     instance.sprint = sprint
    #     instance.nombre = nombre
    #     instance.desarrollador = desarrollador
    #     instance.descripcion = descripcion
    #     if commit:
    #         instance.save()
    #     return instance
