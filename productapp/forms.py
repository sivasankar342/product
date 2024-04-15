from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer']

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['Productname', 'title', 'Productprice','img','category']

class WishlistForm(forms.ModelForm):
  
    class Meta:
        model = Wishlist
        fields = []

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']