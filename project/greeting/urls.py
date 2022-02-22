from django.urls import path
from greeting import views

urlpatterns = [
    path('', views.greeting),
    path('page_4', views.page_4),
    path('json', views.json_reading),
    path('introduction', views.introduction)
]