from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(product)  
admin.site.register(Wishlist) 
admin.site.register(Category)