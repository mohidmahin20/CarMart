from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from owner_app.models import Owner


def user_register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account Created Successfully")
            return redirect("login")
    else:
        register_form = forms.RegistrationForm()
    return render(request, "register.html", {"form": register_form, "type": "Sign Up"})


# class based view number 1
class UserLoginView(LoginView):
    template_name = "register.html"

    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Logged in Successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Logged in information incorrect")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context


@login_required
def profile(request):
    current_user = request.user
    owner_instance = get_object_or_404(Owner, owner=current_user)
    return render(request, "profile.html", {"data": owner_instance})


@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("profile")

    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": profile_form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("home")