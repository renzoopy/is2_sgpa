from os import name
from django.contrib import admin
from django.urls import path, include
from .views import sprint

urlpatterns = [
    path('',sprint,name="sprint"),
]