from django.shortcuts import render

from .models import Post, Comment , Contact

# Create your views here.
def about(request):
    about = "active"
    context = {
        'about':about ,
        
    }
    return render(request,"pages/about.html",context)

def write_for_us(request):
    write_for_us = "active"
    context = {
        'write_for_us':write_for_us 
    }
    return render(request,"pages/write_for_us.html",context)

def tos(request):
    tos = "active"
    context = {
        'tos':tos 
    }
    return render(request,"pages/tos.html",context)

def privacy(request):
    privacy = "active"
    context = {
        'privacy':privacy 
    }
    return render(request,"pages/privacy.html",context)

def contact(request):
    contact = "active"
    context = {
        'contact':contact 
    }

    if request.method == 'POST':
        message = request.POST['message']
        if message != None or message != "":
            name = request.POST['name']
            email = request.POST['email']
            # contact = Contact.objects.create(name=name, email=email, message=message)
            # contact.save()
            print(name, email, message)
            context['message'] = "Your message has been sent successfully"
            return render(request,"pages/contact.html",context)

    context['message'] = ""
    return render(request,"pages/contact.html",context)

def error_404_view(request, exception):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')
