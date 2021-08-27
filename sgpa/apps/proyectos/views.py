from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def nuevoProyecto(request):
    return render(request,'proyectos/nuevoProyecto.html')