from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Product, Wishlist

# Form for user creation
class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_user', 'is_dealer']
        help_texts = {'username': ''}

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pname', 'qty', 'price', 'img']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pname', 'qty', 'price', 'img']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product']

class DeleteWishlistItemForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Confirm Deletion', required=True)