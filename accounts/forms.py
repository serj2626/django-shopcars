from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Введите почту', "class": 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
