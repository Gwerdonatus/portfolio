from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import ContactMessage

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        return render(request, "thank_you.html")
    return render(request, 'contact.html')


