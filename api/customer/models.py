from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

class Order(models.Model):
    customer = models.ForeignKey(to = Customer,on_delete = models.CASCADE)
    item_code = models.CharField(max_length=40)
    quantity = models.IntegerField()

    
    