# Generated by Django 3.2.7 on 2021-10-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_remove_backlog_tareas'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='objetivos',
            field=models.CharField(max_length=300, null=True),
        ),
    ]