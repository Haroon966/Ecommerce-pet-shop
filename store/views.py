from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [{ 'product': p, 'quantity': cart[str(p.id)] } for p in products]
    return render(request, 'store/cart.html', {'cart_items': cart_items})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('product_list')

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after adding
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})
