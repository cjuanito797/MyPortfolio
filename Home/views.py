from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def myProjects(request):
    return render(request, "myProjects.html")