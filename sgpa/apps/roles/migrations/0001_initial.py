# Generated by Django 3.2.6 on 2021-09-03 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('grupo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('proyecto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proyectos.proyecto')),
            ],
            options={
                'permissions': (('Crear proyecto', 'Permite crear proyectos'), ('Modificar proyecto', 'Permite modificar proyectos'), ('Eliminar proyecto', 'Permite eliminar proyectos'), ('Crear Sprint', 'Permite crear un sprint'), ('Modificar Sprint', 'Permite modificar un sprint'), ('Cancelar Sprint', 'Permite cancelar un sprint'), ('Crear user story', 'Permite crear un user story'), ('Modificar user story', 'Permite modificar un user story'), ('Eliminar user story', 'Permite eliminar un user story')),
                'unique_together': {('nombre', 'proyecto')},
            },
        ),
    ]
