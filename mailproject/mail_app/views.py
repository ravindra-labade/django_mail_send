from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


def sending_mail(request):
    template_name = 'mail_app/email.html'
    if request.method == "POST":
        email = request.POST['em']
        username = request.POST['nm']
        subject = 'WELCOME TO MAIL SENDING PROGRAMME'
        message = f'Hi {username}, thank you for receiving my Mail.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse(f"Mail has been sent to {username}")
    return render(request, template_name)
