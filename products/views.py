from django.shortcuts import render

def index(request):
    products = [
        {"name": "Laptop", "price": 3000},
        {"name": "Phone", "price": 2000},
        {"name": "Headphones", "price": 500},
        {"name": "T-Shirt", "price": 120},
        {"name": "Jacket", "price": 350},
        {"name": "Shoes", "price": 400},
        {"name": "Watch", "price": 900},
        {"name": "Bag", "price": 250},
    ]
    return render(request, "products.html", {"products": products})