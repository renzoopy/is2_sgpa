# Generated by Django 3.2.7 on 2021-09-16 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_auto_20210916_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backlog',
            name='tareas',
        ),
    ]
