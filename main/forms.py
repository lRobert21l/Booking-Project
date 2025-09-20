from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Hotel
 
class HotelForm(forms.Form):
    name = forms.CharField(max_length=150, required=True)
    Description = forms.CharField(max_length=50, required=True, widget=forms.Textarea)
    Image = forms.ImageField(required=True)
    Adress = forms.CharField(max_length=255, required=True)
    Mobile = forms.CharField(max_length=15, required=True)
    Email = forms.EmailField(max_length=50, required=True)

class UserRegisterForm(UserCreationForm):
    
    Email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'Email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)