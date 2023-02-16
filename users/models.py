from django.db import models
from django.contrib.auth.models import User


class ContactUs(models.Model): 
    inquiry_title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  
    email = models.EmailField(max_length=200, unique=True) # unique make all email addresses unique, no duplicates. Error caused if duplicate  
    phone = models.CharField(max_length=30) # use CharField for now, then change so it can validate different countries phone numbers 
    message = models.TextField(max_length=1000)   


    def __str__(self): 
        return self.inquiry_title
 
class My_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  
    age = models.IntegerField(null=True, blank=True) 
    phone_number = models.IntegerField(null=True, blank=True) 
    profile_pic = models.ImageField(default = 'default.png', null=True, blank=True)  


    def __str__(self): 
        return self.user.username 
