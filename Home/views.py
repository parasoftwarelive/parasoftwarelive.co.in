from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        "variables":"Hello i am context"
    }
    return render(request, 'home.html', context)
    # return HttpResponse("This is My first page with Asmita")

def services(request):
    context = {
        "variables":"Hello i am context"
    }
    return render(request, 'services.html')

def projects(request):
    context = {
        "variables":"Hello i am context"
    }
    return render(request, 'projects.html')

def contactus(request):
    if request.method == "POST":
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        desc  = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, email=email, desc=desc, date=date)
        contact.save()
        messages.success(request, 'Profile details updated.')
    return render(request, 'contactus.html')
