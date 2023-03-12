from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

state_choices = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]


class Listing(models.Model): 
    user = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150) 
    price = models.IntegerField()
    num_bedrooms = models.IntegerField() 
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    state = models.CharField(max_length=2, blank=True,null=True) 
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
        



        
