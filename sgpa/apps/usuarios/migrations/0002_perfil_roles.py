# Generated by Django 3.2.6 on 2021-09-08 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='roles',
            field=models.ManyToManyField(to='roles.Rol'),
        ),
    ]
