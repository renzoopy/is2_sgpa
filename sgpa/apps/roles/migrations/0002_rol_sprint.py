# Generated by Django 3.2.7 on 2021-09-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_proyecto_equipo'),
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='sprint',
            field=models.ManyToManyField(blank=True, to='proyectos.Sprint'),
        ),
    ]