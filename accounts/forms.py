from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required, Inform a valid email adress.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name', 'email')


class UserProfileForm(forms.ModelForm):
    address = models.CharField(max_length=80)

    class Meta:
        model = UserProfile
        fields = ('address',)
