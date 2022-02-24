from django.urls import path
from first import views

urlpatterns = [
    path('', views.home),
    path('create_task/', views.create_task),
    path('list_tasks/', views.list_tasks),
    path('filter_tasks/', views.filter_tasks),
]