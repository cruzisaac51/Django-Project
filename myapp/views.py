from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask
# Create your views here.

def index(request):
    title = "welcome to Django course !!"
    return render(request, 'index.html', {
        "title": title
    })


def hello(request, username):
    return HttpResponse("<h1>Hello %s </h1>" % username)

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        "projects": projects
    })
    return render(request, 'projects.html', {
        "projects": projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        "tasks": tasks
    })

def create_task(request):
    #new_task = 
    return render(request, "create_task.html", {
        "form": CreateNewTask
    })
