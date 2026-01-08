from django import forms
from .models import Registers, Trainers
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registers
        fields = [
            'first_name', 
            'last_name', 
            'sex', 
            'age', 
            'email', 
            'mobile_number', 
            'address', 
            'join_date'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'join_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainers
        fields = [
            'first_name', 
            'last_name', 
            'sex', 
            'age', 
            'email', 
            'mobile_number', 
            'hire_date'
        ]
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'sex': forms.Select(),
            'age': forms.NumberInput(),
            'email': forms.EmailInput(),
            'mobile_number': forms.TextInput(),
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }