from django.contrib import admin
from productapp.models import CustomUser, Product



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_user', 'is_dealer']



admin.site.register(CustomUser, CustomUserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'qty', 'price']

admin.site.register(Product, ProductAdmin)