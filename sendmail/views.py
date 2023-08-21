from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    send_mail('Tessting Mail Django',
              'I am sending mail using Django application',
              'rakeshibm909@gmail.com',
              ['rakeshgupta5353@gmail.com','bhaktishorts1m@gmail.com']
              ,fail_silently=False)
    return render(request,'home.html')