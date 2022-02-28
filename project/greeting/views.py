from django.shortcuts import render, HttpResponse
import json
from greeting.models import Film

# Create your views here.


def greeting(request):
    text = """
           <!DOCTYPE html>
           <html lang="en">
               <head>
                   <meta charset="UTF-8">
                   <title>Title</title>
                    <link rel="stylesheet" type="text/css" href="/static/css/json_page.css">
                   <ul>
                       <li><a href="page_4">Page_4</a></li>
                      <li><a href="introduction">Introduction</a></li>
                      <li><a href="json">Json</a></li>
                      <li><a href="/greeting">Greeting</a></li>
                      <li><a href="/first">First</a></li>
                    </ul>
               </head>
               <body>
                   <div>
                   HELLO Django
                   </div>
               </body>
           </html>
           """
    return HttpResponse(text)


def introduction(request):
    text = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <link rel="stylesheet" type="text/css" href="/static/css/json_page.css">
                <title>Title</title>
                 <ul>
               <li><a href="page_4">Page_4</a></li>
              <li><a href="introduction">Introduction</a></li>
              <li><a href="json">Json</a></li>
              <li><a href="/greeting">Greeting</a></li>
              <li><a href="/first">First</a></li>
            </ul>
            </head>
            <body>
                <div>
                our new site is made up of Django page
                </div>
            </body>
        </html>
        """
    return HttpResponse(text)


def page_4(request):
    dict_i = dict()
    for i in range(1, 16):
        dict_i[i] = i**2
    print(dict_i)
    return render(request, "file.html", {"dict": dict_i})


def json_reading(request):
    with open('greeting/templates/json_file.json', 'r') as json_file:
        new_json = json.load(json_file)

    return render(request, "json_page.html", {"json": new_json})


def create_film(request):
    name = request.POST.get('film_name', None)
    if name:
        film_name = request.POST.get("film_name")
        film_rate = request.POST.get("film_rate")
        film_is_published = request.POST.get("film_is_published")
        film_status = request.POST.get("film_status")
        film_text = request.POST.get("text")
        url = request.POST.get("url")
        print(url)
        Film.objects.create(name=film_name, rate=film_rate, is_published=film_is_published,
                            status=film_status, text=film_text, geeks_field=url)
    a = render(request, "create_film.html")
    return HttpResponse(a)


def delete_film(request):
    name = request.GET.get('name', None)
    print(name)
    if name:
        Film.objects.filter(name=name).delete()
    a = render(request, "film.html")
    return HttpResponse(a)


def filter_film(request):
    rate = request.GET.get('rate', None)
    if rate:
        response = Film.objects.filter(rate=rate)
    else:
        response = Film.objects.all()
    return render(request, "filter_film.html", {"response": response})


