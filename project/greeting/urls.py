from django.urls import path
from greeting import views

urlpatterns = [
    path('', views.greeting),
    # path('page_4', views.page_4),
    # path('json', views.json_reading),
    # path('introduction', views.introduction),
    path('film', views.create_film),
    path('delete_film', views.delete_film),
    path('filter_film', views.filter_film),

]
