from django.shortcuts import render

# Create your views here.

def sprint(request):
    return render(request,'sprints/sprint.html')