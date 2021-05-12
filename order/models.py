from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cereal.models import Cereal


class Country(models.Model):
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.country


class Address(models.Model):
    street = models.CharField(max_length=255, null=True)
    house_number = models.IntegerField(null=True)
    postal_code = models.IntegerField(null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    order_completed = models.BooleanField(default=False)
    cereal = models.ForeignKey(Cereal, on_delete=models.SET_NULL, null=True)
    order_date_time = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    cereal = models.ForeignKey(Cereal, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
