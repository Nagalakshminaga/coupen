from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


#create your views here.


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request,"about.html")

def image(request):
    return render(request,"image.html")   

def contact(request):
    if request.method=="POST":
      contacts= Contact()
      name=request.POST.get('name')
      email=request.POST.get('email')
      message=request.POST.get('message')
      contacts.name=name
      contacts.email=email
      contacts.message=message
      contacts.save()
      return HttpResponse("<h1><center>Thanks for contact us</center></h1>")
    return render(request,'contact.html')


   