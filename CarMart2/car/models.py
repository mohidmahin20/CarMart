from django.db import models
from brand.models import Brand


# Create your models here.


class Car(models.Model):
    model_name = models.CharField(max_length=30)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to="car/media/uploads/", blank=True, null=True)

    def __str__(self):
        return self.model_name


class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return f"Comments by {self.name}"