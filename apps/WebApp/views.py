from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    return render(request, "home.html")


def store(request):
    return HttpResponse("Store")


def contact(request):
    return HttpResponse("Contact")
