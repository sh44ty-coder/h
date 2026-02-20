from django.shortcuts import render

def category_list(request):
    categories = ["Electronics", "Clothes", "Shoes"]
    return render(request, 'category.html', {'categories': categories})