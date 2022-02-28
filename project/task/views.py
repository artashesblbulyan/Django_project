from django.shortcuts import render,HttpResponse
from task.models import Task
from django.contrib.auth.models import User
# Create your views here.


def task_list(request):
    tasks = Task.objects.all()

    user = User.objects.get(id=1)
    return render(request, "task/home.html", context={"task_list": tasks, 'user': user})
