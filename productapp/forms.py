from django import forms
from .models import CustomUser, Product, Wishlist

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