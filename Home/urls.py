from django.urls import path, re_path

from . import views

app_name = 'home'

urlpatterns = [
    path("", views.home, name="home"),
    path("myProjects/", views.myProjects, name="myProjects"),


]

