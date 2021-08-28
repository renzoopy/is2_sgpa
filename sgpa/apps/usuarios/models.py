from django.db import models
from django.contrib.auth.models import User
from roles.models import Rol

# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.PositiveIntegerField(null=False, blank=False, unique=True, error_messages={"unique":"CI no disponible"})
    telefono = models.PositiveIntegerField(blank=False, null=True)
    roles = models.ManyToManyField(Rol)

    class Meta:
        permissions = ( ("acceso_usuario", "Permite el acceso al SGAP"),
                        ("editar_usuario", "Permite editar usuario"),
                        ("eliminar_usuario", "Permite eliminar usuario"))

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)