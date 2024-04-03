from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('user','User'),
        ('dealer','Dealer'),
       
       
    )
   
    user=models.BooleanField(default=False)
    dealer=models.BooleanField(default=False)



class product(models.Model):
   # id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.URLField(max_length=100)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)