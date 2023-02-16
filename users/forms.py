from django.forms import ModelForm 
from django import forms 
from .models import ContactUs, My_profile
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 


class ContactUsForm(ModelForm): 
    class Meta: 
        model = ContactUs 
        fields = ["inquiry_title", "first_name", "last_name", "email", "phone", "message"] 


class FormUserCreation(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] 

class CustomUserChangeForm(UserChangeForm,): 
    profile_pic = forms.ImageField(required=False)
    age = forms.IntegerField(required=False)
    phone_number = forms.IntegerField(required=False)

    class Meta: 
        model = User
        fields = ['profile_pic','first_name', 'last_name', 'age', 'email', 'phone_number'] 


