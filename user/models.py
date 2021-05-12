from django.contrib.auth.models import User
from django.db import models
from cereal.models import Cereal
from order.models import Address


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    favorite_cereal = models.ForeignKey(Cereal, on_delete=models.SET_NULL, null=True)
    profile_image = models.CharField(max_length=9999, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)


class Search(models.Model):
    search_query = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
