# Generated by Django 3.2.7 on 2021-09-07 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_perfil_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ['id'], 'permissions': (('autorizar_usuario', 'Permite la administración del SGPA'), ('acceso_usuario', 'Permite el acceso a SGPA'), ('editar_usuario', 'Permite editar usuario'), ('eliminar_usuario', 'Permite eliminar usuario'))},
        ),
    ]
