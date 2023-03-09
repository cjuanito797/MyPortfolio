from django.shortcuts import render
from .forms import ContactMe
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render (request, "home.html")


def myProjects(request):
    return render (request, "myProjects.html")


def contactMe(request):
    # pass in our contact me form here for processing

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['cjuangas17@gmail.com'],
            fail_silently=False
        )

        return redirect('home:home')

    return render (request, "contactMe.html")
