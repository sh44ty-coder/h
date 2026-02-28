from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, "products.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "success.html")

    return render(request, "contact.html")