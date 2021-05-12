from django.db import models
from django.contrib.auth.models import User
from cereal.models import Cereal

# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartCereal(models.Model):
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
