from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
import datetime
from django.urls import path, include

# Create your views here.


def home(request):

    return HttpResponse("HOME")


