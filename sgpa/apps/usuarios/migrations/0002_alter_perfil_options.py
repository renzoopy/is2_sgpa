# Generated by Django 3.2.6 on 2021-09-02 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'permissions': (('editar_usuario', 'Permite editar usuario'), ('eliminar_usuario', 'Permite eliminar usuario'))},
        ),
    ]
