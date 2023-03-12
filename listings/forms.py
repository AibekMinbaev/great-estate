from django.forms import ModelForm 
from django import forms
from .models import Listing, state_choices


class ListingForm(ModelForm): 
    state = forms.ChoiceField(choices= state_choices, required=True)
    class Meta: 
        model = Listing 
        fields = ["title", "price","state","num_bedrooms", "num_bathrooms", "square_footage", "address", "property_image"] 
