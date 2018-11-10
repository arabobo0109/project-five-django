from django.shortcuts import render, get_object_or_404
from .models import Product
from checkout.models import OrderLineItem

def all_products(request):
    """
    Lists all products
    """
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    
def product_detail(request, pk):
    """
    Creates a page with full product details
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {'product': product})
    
# def get_order_total
    # total = OrderLineItem.objects.filter
    # filter by product name - depending on the id of the page 
    # add together the total amount of orders for that item 
    
# Import OrderLineItem from checkout models.py, filter by name of product, then add together the total amount of orders for that item.