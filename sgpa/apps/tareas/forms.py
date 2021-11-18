from django import forms
from django.db.models import Q
from miembros.models import Miembro
from usuarios.models import Perfil
from tareas.models import UserStory
from django.forms import Form, CharField, IntegerField


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


class UserStoryEdit_Form(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = [
            "nombre",
            "descripcion",
            "estado",
            "desarrollador",
        ]
        labels = {
            "nombre": "Nombre",
            "descripcion": "Descripcion",
            "estado": "Estado",
            "desarrollador": "Desarrollador",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.Select(attrs={"class": "form-control"}),
            "desarrollador": forms.Select(attrs={"class": "form-control"}),
        }

        def init(self, args, **kwargs):
            super(UserStoryEdit_Form, self).init(args, **kwargs)
            self.fields["desarrollador"].queryset = Miembro.objects.filter(~Q(id=1))
