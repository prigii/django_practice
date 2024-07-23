from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, World")

def about(request):
    return HttpResponse("This is the about page")

def contact(request):
    return HttpResponse("This is the contact page") 

