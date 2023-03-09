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
        form = ContactMe(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            plaintext = get_template ('email.txt')
            htmlEmail = get_template ('email.html')

            content = ({
                'sender': sender,
                'subject': subject,
                'message': message
            })

            text_content = plaintext.render (content)
            html_content = htmlEmail.render (content)
            reciever = 'cjuangas17@gmail.com'
            msg = EmailMultiAlternatives ("Appointment has been re-scheduled", html_content,
                                      settings.EMAIL_HOST_USER,
                                      [reciever])

            msg.attach_alternative (html_content, "text/html")
            msg.send ( )

        return redirect ('home:home')


    else:
        form = ContactMe ( )

    return render (request, "contactMe.html", {'form': form})
