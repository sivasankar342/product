from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class YourModel(models.Model):
    created_at = models.DateTimeField(default=datetime.now)


class User(AbstractUser):
    class Role(models.TextChoices):
        USERS = 'USERS', 'User'
        DEALER = 'DEALER', 'Dealer'
        ADMIN = 'ADMIN',  'admin'

    is_dealer = models.BooleanField(default=False)
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.USERS)
class Category(models.Model):
   
    category=models.CharField(max_length=100,unique=True)


    def _str_(self):
        return self.category

class product(models.Model):
    Productname = models.CharField(max_length=100)
    title = models.TextField()
    Productprice = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.URLField(max_length=100)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(product, blank=True) 

    def _str_(self):
        return f"Wishlist for {self.user.username}"