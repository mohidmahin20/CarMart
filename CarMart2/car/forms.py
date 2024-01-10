from django import forms
from .models import Car, Comment


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ["brand_name"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "body"]