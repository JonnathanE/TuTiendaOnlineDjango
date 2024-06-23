from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data["name"]
            email = contact_form.cleaned_data["email"]
            message = contact_form.cleaned_data["message"]
            # print(name, email, message)
            # send email
            emial = EmailMessage(
                subject="TuTiendaOnline send a message contact",
                body="The user {} whit email {} send: \n\n {}".format(
                    name, email, message
                ),
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )
            try:
                emial.send()
                messages.success(request, "Your message has been sent")
            except Exception as e:
                print(e)
                messages.error(request, "Error sending message")

            # return render(request, "contact/home_contact.html", {"contact_form": contact_form})
            return redirect("/contact/")
    return render(request, "contact/home_contact.html", {"contact_form": contact_form})
