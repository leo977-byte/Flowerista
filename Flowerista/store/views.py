from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Cart, CartItem, ProductVariant

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto log-in after signing up
            return redirect('home')
        else:
            # Pass form errors back to template
            return render(request, 'signup.html', {'form': form, 'errors': form.errors})
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'errors': "Invalid username or password."})
    return render(request, 'login.html')


def product_detail(request, slug="lilies"):
    # Try fetching product from DB, or pass None if it doesn't exist yet
    product = Product.objects.filter(slug=slug).first()
    variants = product.variants.all() if product else []
    
    if request.method == 'POST':
        return redirect('cart')
        
    return render(request, 'product_detail.html', {
        'product': product, 
        'variants': variants
    })
def cart_view(request):
    if request.method == 'POST':
        # Handles "Proceed to Checkout" button submit
        return redirect('cart')
    return render(request, 'cart.html')

def checkout_view(request):
    if request.method == 'POST':
        return render(request, 'checkout.html', {'success': True})
    return render(request, 'checkout.html')

def create_flower_view(request):
    return render(request, 'create_flower.html')