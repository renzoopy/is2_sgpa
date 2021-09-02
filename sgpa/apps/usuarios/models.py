from django.db import models
from django.contrib.auth.models import User
from roles.models import Rol

# Create your models here.


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.PositiveIntegerField(
        null=False,
        blank=False,
        unique=True,
        error_messages={"unique": "CI no disponible"},
    )
    roles = models.ManyToManyField(Rol)
    telefono = models.PositiveIntegerField(blank=False, null=True)

    class Meta:
        permissions = (
            ("editar_usuario", "Permite editar usuario"),
            ("eliminar_usuario", "Permite eliminar usuario"),
        )

    def __str__(self):
        return "{} {}".format(self.usuario.first_name, self.usuario.last_name)
