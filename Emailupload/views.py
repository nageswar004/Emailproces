from django.shortcuts import render
from django.http import HttpResponse
#from Emailupload import templates
from Emailproces import settings
from django.core.mail import send_mail
# Create your views here.

def mail(request):
    subject='Greetings'
    msg    = "Congratulations your sucess"
    to     = "nageswar004@gmail.com"
    res    = send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if(res==1):
        msg="Mail send sucessfully"
    else:
        msg=" Mail Could not Sent"

    return HttpResponse(msg)
