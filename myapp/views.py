from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask
from .forms import CreateNewProject
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
    return render(request, 'projects/projects.html', {
        "projects": projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        "tasks": tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, "tasks/create_task.html", {
        "form": CreateNewTask
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect("Tasks")


def create_project(request):
    if request.method == 'GET':
        return render(request, "projects/create_project.html", {
            "form": CreateNewProject
        })
    else:
        Project.objects.create(name= request.POST["name"])
        redirect("Projects")


