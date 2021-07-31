from django import forms
from django.forms import ModelForm
from .models import*


#user loging form
class UserLogingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':"Your User Email Id", 'required':'True'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder':"Enter Password", 'required':'True'}))


#user password forms
class UserPassForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder':"Enter Password", 'required':'True'}))
    repassword = forms.CharField(max_length=50, label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder':"Enter Password", 'required':'True'}))




