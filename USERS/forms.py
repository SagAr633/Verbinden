from django import forms
from USERS.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import ValidationError


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'phone',
            'username',
            'password1',
            'password2',
        ]


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
