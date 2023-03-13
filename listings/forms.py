from django.forms import ModelForm 
from django import forms
from .models import Listing 
from localflavor.us.us_states import STATE_CHOICES


class ListingForm(ModelForm): 
    state = forms.ChoiceField(choices= STATE_CHOICES, required=True)
    city = forms.ChoiceField(choices=[]) 
    class Meta: 
        model = Listing 
        fields = ["title", "price","state","num_bedrooms", "num_bathrooms", "square_footage", "address", "property_image"] 
