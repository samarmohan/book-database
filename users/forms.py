from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Add email to Django built in user form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]
