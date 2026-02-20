from django.shortcuts import render

def index(request):
    categories = [
        "Electronics",
        "Clothes",
        "Shoes"
    ]
    return render(request, "category.html", {"categories": categories})