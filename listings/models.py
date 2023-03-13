from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Listing(models.Model): 
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150) 
    price = models.IntegerField()
    num_bedrooms = models.IntegerField() 
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    state = models.CharField(max_length=2, blank=True,null=True)
    city = models.CharField(max_length=120, blank=True, null=True) 
    street = models.CharField(max_length=120, blank=True, null=True)  
    address = models.CharField(max_length=120) # more clear address with real streets home and address 
    property_image = models.ImageField(default = 'defaultproperty.jpg', blank=True, null=True) # adding multiple images
    
    def __str__(self): 
        return self.title 

class Listing_rent(models.Model): 
    title = models.CharField(max_length=150) 
    price = models.IntegerField() 
    num_bedrooms = models.IntegerField() 
    num_bathrooms = models.IntegerField() 
    square_footage = models.IntegerField() 
    address = models.CharField(max_length=120) 
    property_image = models.ImageField(default = 'defaultproperty.jpg', blank=True, null=True)

    def __str__(self): 
        return self.title 
        



        
