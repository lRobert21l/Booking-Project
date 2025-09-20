from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    
    Email = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['username', 'Email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class SearchForm(forms.Form):
    query = forms.CharField(
        label="Oraș",
        widget=forms.TextInput(attrs={"placeholder": "Introduceți orașul..."})
    )
    date = forms.DateField(
        label="Data",
        widget=forms.DateInput(attrs={"type": "date"})
    )