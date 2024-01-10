from django.urls import path
from . import views

urlpatterns = [
    path("buy_now/<int:id>/", views.buy_now, name="buy_now"),
]