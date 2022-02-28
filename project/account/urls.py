from django.urls import path
from account import views

urlpatterns = [
    path('', views.new_account),
    # path('new_accout', views.delete_film),


]
