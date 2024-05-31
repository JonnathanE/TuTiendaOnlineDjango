from django.shortcuts import render

from .models import Service


# Create your views here.
def services(request):
    services = Service.objects.all()
    return render(request, "services/home_services.html", {"services": services})
