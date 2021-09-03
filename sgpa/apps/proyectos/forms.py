from django import forms
from proyectos.models import Proyecto
from usuarios.models import Perfil
from django.db.models import Q


class ProyectoAdminForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super(ProyectoAdminForm, self).__init__(*args, *kwargs)
        self.fields["scrumMaster"].queryset = Perfil.objects.filter(~Q(ide=1))


class ProyectoMasterForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = fields = ["nombre", "descripcion", "numSprints"]
        labels = {
            "nombre": "Nombre",
            "descripcion": "Descripcion",
            "numSprints": "NúmeroSprint",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "numSprints": forms.NumberInput(attrs={"class": "form-control"}),
        }
