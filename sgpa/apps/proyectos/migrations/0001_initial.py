# Generated by Django 3.2.6 on 2021-09-03 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numTareas', models.IntegerField(default=0)),
                ('estado', models.CharField(default='En cola', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=200)),
                ('fechaCreacion', models.DateField(auto_now_add=True)),
                ('fechaInicio', models.DateField(null=True)),
                ('fechaFin', models.DateField(null=True)),
                ('estado', models.CharField(default='Pendiente', max_length=10)),
                ('numSprints', models.IntegerField(default=1)),
                ('scrumMaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfil')),
            ],
        ),
    ]
