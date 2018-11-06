from django.shortcuts import render
from ecommerce.models import Product
from posts.models import Post
from django.db.models import Q

def do_search(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['q']) | Q(strap__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    posts = Post.objects.filter(Q(name__icontains=request.GET['q']) | Q(strap__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    return render(request, "products.html", {"products":products})
    