from django import forms
from django.contrib.auth.models import User
from .models import Agent, Booking


class RegisterForm(forms.ModelForm):
    """docstring for Register Agent Form"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class BookEvent(forms.ModelForm):
    """docstring for Booking Event Form"""
    class Meta:
            model = Booking
            fields = ('dob', 'event')
            widgets = {
                'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                'event': forms.TextInput(attrs={'class': 'form-control'}),
            }
