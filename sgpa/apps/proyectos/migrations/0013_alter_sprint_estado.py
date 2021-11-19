# Generated by Django 3.2.7 on 2021-11-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0012_alter_backlog_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprint',
            name='estado',
            field=models.CharField(choices=[('En_cola', 'En cola'), ('Activo', 'Activo'), ('Cancelado', 'Cancelado'), ('Finalizado', 'Finalizado')], default='En_cola', max_length=10),
        ),
    ]
