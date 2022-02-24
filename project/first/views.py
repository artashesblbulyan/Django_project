from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
import datetime
from django.urls import path, include
from first.models import Task
# Create your views here.


def home(request):

    return HttpResponse("HOME")


def create_task(request):
    task_name = "python 3 "
    description = "look into docs"
    status = 2

    # task =Task(name=task_name, description=description, status=status)
    # task.save()

    # task = Task.objects.create(name=task_name, description=description, status=status)

    return HttpResponse("succes {}".format(task))


def list_tasks(request):
    # tasks = Task.objects.all()
    tasks = Task.objects.filter(status=2)
    response = ""
    for i in tasks:
        response += str(i) + "<br>"
    print(request.__dict__)
    print(request.GET)
    return HttpResponse(response)


def filter_tasks(request):
    name = request.GET.get('name', None)
    if name:
        response = Task.objects.filter(name=name)
    else:
        response = Task.objects.all()

    return HttpResponse(response)
