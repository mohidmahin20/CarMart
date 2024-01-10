from django.shortcuts import redirect
from . import models
from django.contrib import messages
from car.models import Car
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def buy_now(request, id):
    car = Car.objects.get(pk=id)
    owner, create = models.Owner.objects.get_or_create(owner=request.user)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        if car not in owner.purchased_cars.all():
            owner.purchased_cars.add(car)
        messages.success(request, "Buy car Successful")
        return redirect("profile")
    else:
        messages.warning(request, "Out of the stock")
        return redirect("home")