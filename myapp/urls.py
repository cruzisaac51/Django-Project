from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="Home"),
    path("hello/<str:username>", views.hello),
    path("projects/", views.projects, name="Projects"),
    path("tasks/", views.tasks, name="Tasks"),
    path("create_task/", views.create_task, name= "create_new_Task"),
    path("create_project/", views.create_project, name= "create_new_Project"),
    path("signup/", views.signup, name="Signup"),
]   