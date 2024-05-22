from django.shortcuts import render, redirect



def IndexPage(request):
    return render(request, 'index.html')




def AboutPage(request):
    return render(request, 'about.html')



def ApiPage(request):
    return render(request, 'api.html')




def ContactPage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if len(message) !=0:
            pass
        return redirect('contact')
    return render(request, 'contact.html')