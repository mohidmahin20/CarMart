from django.db import models
from django.contrib.auth.models import User
from car.models import Car


# Create your models here.
class Owner(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    purchased_cars = models.ManyToManyField(Car, blank=True)

    def __str__(self):
        return self.owner.username