from os import name
from django.contrib import admin
from django.urls import path, include
from .views import base, nuevoProyecto

urlpatterns = [
    path('',base,name="base"),
    path('nuevo/',nuevoProyecto,name="nuevoProyecto"),
]