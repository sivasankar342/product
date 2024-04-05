"""
URL configuration for file project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productapp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for admin site
    path('', views.registration, name='registration'),  # URL for registration page
    path('homepage/', views.homepage, name='homepage'),  # URL for homepage
    path('loginpage/', views.loginpage, name='loginpage'),  # URL for login page
    path('userdashboard/', views.userdashboard, name='userdashboard'),  # URL for user dashboard
    path('dealerdashboard/', views.dealerdashboard, name='dealerdashboard'),  # URL for dealer dashboard
    path('logoutpage/', views.logoutpage, name='logoutpage'),  # URL for logout page
    path('create_product/', views.create_product, name='create_product'),  # URL for creating a product
    path('productlist/', views.productlist, name='productlist'),  # URL for list of products
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),  # URL for adding product to wishlist
    path('wishlist/', views.wishlist, name='wishlist'),  # URL for wishlist
    path('remove_from_wishlist/', views.remove_from_wishlist, name='remove_from_wishlist'),  # URL for removing from wishlist
]