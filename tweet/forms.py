from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']
        widgets = {
            'text': forms.Textarea(attrs={
            'class': 'form-control block item-align-center',
            'placeholder': 'Enter your tweet here...',
            'rows': 4,
            'cols': 45,
            }),
            'photo': forms.FileInput(attrs={
            'class':'form-control block ',
            'accept': 'image/*',
            }),
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={
            'class': 'form-control block item-align-center',
            'placeholder': 'Enter your username here...',
            'rows': 1,
            'cols': 45,
            }),
            'email': forms.EmailInput(attrs={
            'class': 'form-control block item-align-center',
            'placeholder': 'Enter your email here...',
            'rows': 1,
            'cols': 45,
            }),
            'password1': forms.PasswordInput(attrs={
            'class': 'form-control block item-align-center',
            'placeholder': 'Enter your password here...',
            'rows': 1,
            'cols': 45,
            }),
            'password2': forms.PasswordInput(attrs={
            'class': 'form-control block item-align-center',
            'placeholder': 'Confirm your password here...',
            'rows': 1,
            'cols': 45,
            }),
        }

class SearchForm(forms.Form):
    query=forms.CharField(max_length=100)