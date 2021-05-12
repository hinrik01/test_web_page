from django.db import models

# Create your models here.


class CerealCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cereal(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=9999, blank=True)
    price = models.IntegerField()
    ingredients = models.CharField(max_length=9999)
    weight = models.IntegerField()
    sugar = models.IntegerField()
    category = models.ManyToManyField(CerealCategory)

    def __str__(self):
        return self.name


class CerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(Cereal, on_delete=models.CASCADE)

    def __str__(self):
        return self.image



