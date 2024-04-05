from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm, ProductCreationForm, WishlistForm
from .models import Product, Wishlist


def homepage(request):
    return render(request, 'homepage.html')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('loginpage'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

#
@login_required
def userdashboard(request):
    return render(request, 'userdashboard.html', {'username': request.user.username})


@login_required
def dealerdashboard(request):
    if request.user.is_dealer:
        return redirect('create_product')
    return render(request, 'dealerdashboard.html', {'username': request.user.username})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('un')
        password = request.POST.get('pw')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('dealerdashboard' if user.is_dealer else 'userdashboard'))
    return render(request, 'login.html')


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
def add_to_wishlist(request):
    form = WishlistForm()
    
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist_item=form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.Product = Product
            wishlist_item.save()
            return redirect('wishlist')
    
        
    return render(request, 'add_to_wishlist.html', {'form': form})

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = Wishlist.objects.get(pk=wishlist_item_id, user=request.user)
    if request.method == 'POST':
        wishlist_item.delete()
        return redirect('wishlist')
    return render(request, 'remove_from_wishlist.html', {'wishlist_item': wishlist_item})