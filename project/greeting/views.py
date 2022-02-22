from django.shortcuts import render,HttpResponse
import json
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
