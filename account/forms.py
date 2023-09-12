from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Loginform(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"login_input login__group login__group__input login__group__label"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"login_input login__group login__group__input login__group__label"}))

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']