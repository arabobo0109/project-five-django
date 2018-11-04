from django.shortcuts import render
from ecommerce.models import Product
from posts.models import Post
from django.db.models import Q

def do_search(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['q']) | Q(strap__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    return render(request, "products.html", {"products":products})
    
def do_post_search(request):
    posts = Post.objects.filter(Q(title__icontains=request.GET['q']) | Q(content__icontains=request.GET['q']))
    return render(request, "postdetail.html", {"posts":posts})