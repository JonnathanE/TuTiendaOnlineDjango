from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return HttpResponse("INICIO")


def services(request):
    return HttpResponse("Services")


def store(request):
    return HttpResponse("Store")


def blog(request):
    return HttpResponse("Blog")


def contact(request):
    return HttpResponse("Contact")
