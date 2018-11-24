from django.shortcuts import render
from ecommerce.models import Product
from posts.models import Post
from content.models import Content
from django.db.models import Q

# def do_search(request):
    
#     results = {
#         'products': None, 
#         'posts': None, 
#         'content': None,
#     }
    
#     products = Product.objects.filter(Q(name__icontains=request.GET['q']) | Q(strap__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
#     posts = Post.objects.filter(Q(title__icontains=request.GET['q']) | Q(content__icontains=request.GET['q']))
#     content = Content.objects.filter(Q(title__icontains=request.GET['q']) | Q(strapline__icontains=request.GET['q']) | Q(article__icontains=request.GET['q']))
    
#     results['products'] = products
#     results['posts'] = posts
#     results['content'] = content
    
#     return render(request, "products.html", {"results": results})


# def do_search(request):
    
#     results = {
#         'products': None, 
#         # 'posts': None, 
#         # 'content': None,
#     }
    
#     products = Product.objects.filter(Q(name__icontains=request.GET['q']) | Q(strap__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
#     # posts = Post.objects.filter(Q(title__icontains=request.GET['q']) | Q(content__icontains=request.GET['q']))
#     # content = Content.objects.filter(Q(title__icontains=request.GET['q']) | Q(strapline__icontains=request.GET['q']) | Q(article__icontains=request.GET['q']))
    
#     results['products'] = products
#     # results['posts'] = posts
#     # results['content'] = content
    
#     return render(request, "products.html", {"results": results})


def do_search_products(request):
    products = Product.objects.filter(Q(name__icontains=request.GET['q']) | Q(strap__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    return render(request, "products.html", {"products":products})