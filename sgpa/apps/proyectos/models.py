from usuarios.models import Perfil
from django.db import models
from django.core.validators import MinValueValidator

ESTADOPROY_CHOICES = [
    ("En espera", "En espera"),
    ("En desarrollo", "En desarrollo"),
    ("Cancelado", "Cancelado"),
    ("Culminado", "Culminado"),
]

ESTADOSPR_CHOICES = [
    ("En cola", "En cola"),
    ("Activo", "Activo"),
    ("Cancelado", "Cancelado"),
    ("Finalizado", "Finalizado"),
]

# Create your models here.


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(max_length=200, blank=False)
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaInicio = models.DateField(null=True)
    fechaFin = models.DateField(null=True)
    estado = models.CharField(default="Pendiente", max_length=10)
    numSprints = models.IntegerField(default=1)
    scrumMaster = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nombre)


class Sprint(models.Model):
    numTareas = models.IntegerField(default=0)
    estado = models.CharField(max_length=7, default="En cola")

    def __str__(self):
        return "{}".format(self.estado)
