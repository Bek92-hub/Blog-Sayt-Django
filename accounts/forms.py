from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): # registration
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name','last_name','email', 'age',)

class CustomUserChangeForm(UserChangeForm): # changes - измененияpython manage.py makemigrations

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name','email', 'age',)