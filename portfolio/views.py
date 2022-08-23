from email import message
from django.shortcuts import render
from .models import Contact



def home(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts':contacts})

def about(request):
    contacts = Contact.objects.all()
    return render(request, 'about.html', {'contacts':contacts})

def ourwork(request):
    contacts = Contact.objects.all()
    return render(request, 'furniture.html', {'contacts':contacts})

def contact(request):
    if request.method=="POST":
        message  = request.POST.get("message","")
        name  = request.POST.get("username","")
        phone  = request.POST.get("phone","")
        email  = request.POST.get("email","")
        
        response = Contact(name = name, phone = phone, email = email, message = message)
        response.save()
    return render(request, 'contact.html')