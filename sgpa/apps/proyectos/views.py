from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def proyectos(request):
    return render(request,'proyectos/proyectos.html')

def nuevoProyecto(request):
    return render(request,'proyectos/nuevoProyecto.html')