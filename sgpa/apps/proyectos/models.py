from django.db import models

ESTADOPY_CHOICES = [  ("En espera","En espera"),
                    ("En desarrollo", "En desarrollo"),
                    ("Cancelado","Cancelado"),
                    ("Culminado","Culminado")
]

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(max_length=200, blank=False)
    fechaCreacion = models.DateField(auto_now_add=True)
    fechaInicio = models.DateField(null=True)
    fechaFin = models.DateField(null=True)
    estado = models.CharField(default='Pendiente', max_length=10)

    def __str__(self):
        return '{}'.format(self.nombre)