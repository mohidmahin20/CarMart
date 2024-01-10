from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.profile, name="profile"),
    path("profile/edit", views.edit_profile, name="edit_profile"),
    path("register/", views.user_register, name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
]