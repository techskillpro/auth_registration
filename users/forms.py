from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length = 100)
    home_address = forms.CharField(max_length = 500)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'home_address', 'password1', 'password2']
