from django.shortcuts import render, redirect
from .models import Contact


def IndexPage(request):
    return render(request, 'index.html')




def AboutPage(request):
    return render(request, 'about.html')



def ApiPage(request):
    return render(request, 'api.html')




def ContactPage(request):
    a = Contact()
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if len(message) !=0:
            Contact.objects.create(name=name, phone_number=phone, email=email, message=message)
            return redirect('index')
        else:
            return redirect('index')
    return render(request, 'contact.html')