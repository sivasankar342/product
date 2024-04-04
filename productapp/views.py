from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from productapp.forms import CustomUserCreationForm, ProductCreationForm, WishlistForm
from productapp.models import Product, Wishlist

def homepage(request):
    return render(request, 'homepage.html')

def registration(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('loginpage')
    return render(request, 'registration.html', {'form': form})


@login_required
def userdashboard(request):
    return render(request, 'userdashboard.html', {'username': request.user.username})

@login_required
def dealerdashboard(request):
    return render(request, 'dealerdashboard.html', {'username': request.user.username})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pw')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('dealerdashboard' if user.is_dealer else 'userdashboard'))
    return render(request, 'loginpage.html')

@login_required
def logoutpage(request):
    logout(request)
    return render(request, 'logoutpage.html')

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Product successfully added....')
    else:
        form = ProductCreationForm()
    return render(request, 'create_product.html', {'form': form})

@login_required
def productlist(request):
    products = Product.objects.all() 
    return render(request, 'productlist.html', {'products': products})

@login_required
def add_to_wishlist(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.product = product
            wishlist_item.save()
            return redirect('wishlist')
    else:
        form = WishlistForm()
    return render(request, 'add_to_wishlist.html', {'form': form})

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})