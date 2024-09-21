from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)



class Order(models.Model):
    user =  models.ForeignKey(Customer,  on_delete=models.CASCADE)
    address= models.CharField(max_length=200)
    status= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Item(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity= models.CharField(max_length=10)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)