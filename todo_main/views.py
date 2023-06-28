

from django.shortcuts import render
from todo.models import Task

def home(request):
    
    tasks = Task.objects.filter(is_completed=False)
    return render(request, 'home.html', {"tasks": tasks})