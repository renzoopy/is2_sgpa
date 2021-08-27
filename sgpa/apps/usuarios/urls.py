from os import name
from django.contrib import admin
from django.urls import path, include
from .views import index,home

urlpatterns = [
    path('',index,name="login"),
    path('home/',home,name="home")
]