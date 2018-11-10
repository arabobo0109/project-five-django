from django.shortcuts import render, redirect, reverse
from django.contrib import messages

def view_cart(request):
    """Renders the contents of the cart, to 'cart.html'"""
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
    
def adjust_cart(request, id):
    """Allows the user to adjust the quantity of items in the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))