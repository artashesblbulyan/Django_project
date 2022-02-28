from django.shortcuts import render,HttpResponse


def new_account(request):
    return render(request,"account/index.html")

