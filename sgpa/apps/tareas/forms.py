from django import forms
from tareas.models import UserStory


class UserStoryForm(forms.ModelForm):
    identificacion = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"})
    )

    def __init__(self, *args, **kwargs):
        # super(UserStoryForm, self).__init__(*args, **kwargs)
        super(UserStoryForm, self).init(args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        sprint = kwargs.get("sprint")
        nombre = kwargs.get("nombre")
        desarrollador = kwargs.get("desarrollador")
        descripcion = kwargs.get("descripcion")
        instance = super(UserStoryForm, self).save(commit=False)
        instance.sprint = sprint
        instance.nombre = nombre
        instance.desarrollador = desarrollador
        instance.descripcion = descripcion
        if commit:
            instance.save()
        return instance
