from django.shortcuts import render
from ecommerce.models import Product

def search_page(request):
    """Loads a page the user can search the website from"""
    return render(request, 'search.html')

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products":products})