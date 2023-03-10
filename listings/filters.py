import django_filters 
from .models import * 

class BuyFilter(django_filters.FilterSet): 
    class Meta: 
        model = Listing 
        fields = {"price": ['lt', 'gt'], "num_bedrooms": ['exact'], "num_bathrooms" : ['exact'], 'square_footage':['lt', 'gt']} 
