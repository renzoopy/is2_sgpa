from django.urls import path, include
from .views import base

urlpatterns = [
    path('',base,name="base"),
]