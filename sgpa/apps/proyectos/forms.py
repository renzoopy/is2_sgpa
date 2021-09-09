from django import forms
from django.db.models import Q
from usuarios.models import Perfil
from proyectos.models import Proyecto, Sprint


class Proyecto_Form(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion", "scrumMaster"]
        labels = {
            "nombre": "Nombre",
            "descripcion": "Descripcion",
            "scrumMaster": "Scrum Master",
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "scrumMaster": forms.Select(attrs={"class": "form-control"}),
        }

    def init(self, args, **kwargs):
        super(Proyecto_Form, self).init(args, **kwargs)
        self.fields["scrumMaster"].queryset = Perfil.objects.filter(~Q(id=1))


class Sprint_Form(forms.ModelForm):
    class Meta:
        model = Sprint
        fields = [
            "estado",
            "numTareas",
        ]
        labels = {
            "estado": "Estado",
            "numTareas": "Número de Tareas",
        }