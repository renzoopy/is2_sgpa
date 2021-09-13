from django.contrib.auth.models import Group, User
from django.db.models.deletion import CASCADE
from usuarios.models import Perfil
from django.db import models

ESTADOPROY_CHOICES = [
    ("Pendiente", "Pendiente"),
    ("Iniciado", "Iniciado"),
    ("Cancelado", "Cancelado"),
    ("Finalizado", "Finalizado"),
]

ESTADOSPR_CHOICES = [
    ("En_cola", "En_cola"),
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
    estado = models.CharField(
        default="Pendiente",
        max_length=10,
        null=False,
        blank=False,
        choices=ESTADOPROY_CHOICES,
    )
    numSprints = models.IntegerField(default=0)
    scrumMaster = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    equipo = models.OneToOneField(Group, on_delete=models.CASCADE, null=True)

    def str(self):
        return "{}".format(self.nombre)


class Sprint(models.Model):
    numTareas = models.IntegerField(default=0)
    duracion = models.IntegerField(default=0)
    estado = models.CharField(max_length=10, default="En_cola")
    proyecto = models.ForeignKey(
        Proyecto, null=True, blank=False, on_delete=models.CASCADE
    )

    def str(self):
        return "{}".format(self.estado)
