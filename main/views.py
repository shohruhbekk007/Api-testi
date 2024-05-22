from django.shortcuts import render



def IndexPage(request):
    return render(request, 'index.html')




def AboutPage(request):
    return render(request, 'about.html')



def ApiPage(request):
    return render(request, 'api.html')




def ContactPage(request):
    return render(request, 'contact.html')