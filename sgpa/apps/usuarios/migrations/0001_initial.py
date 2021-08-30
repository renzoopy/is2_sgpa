# Generated by Django 3.2.6 on 2021-08-28 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.PositiveIntegerField(error_messages={'unique': 'CI no disponible'}, unique=True)),
                ('telefono', models.PositiveIntegerField(null=True)),
                ('roles', models.ManyToManyField(to='roles.Rol')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('acceso_usuario', 'Permite el acceso al SGAP'), ('editar_usuario', 'Permite editar usuario'), ('eliminar_usuario', 'Permite eliminar usuario')),
            },
        ),
    ]
