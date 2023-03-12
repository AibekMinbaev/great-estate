from django.shortcuts import render, redirect 
from .models import Listing, Listing_rent 
from .forms import ListingForm 
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users 
from .filters import BuyFilter
from django.core.paginator import Paginator 


# Create your views here.
# CGUD - create, read, update, delete and list(will show all the elements) 

state_dict = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}



def listing_list(request): # this function will list out all elements in listing database 
    #filter_data = request.session.get('filter_data')
    #print(filter_data) # working until here. How to give this data as a initial data for the BuyFilter? ?  

    listings = Listing.objects.all() # list of all objects 
    
    buy_filter = BuyFilter(request.GET, queryset=listings) # django_filter is no a form, it is a class object ??    
    
    listings = buy_filter.qs
    
    p = Paginator(listings, 2) 
    page = request.GET.get('page') 
    listing_list = p.get_page(page) 
    
    context = { "listings" : listings, 'buy_filter': buy_filter, 'listing_list': listing_list}
    return render(request, "listings.html", context)  


def listing_retrieve(request, pk): # this function will list a signle element by id 
    listing = Listing.objects.get(id=pk) 
    if listing.state != None: 
        state = state_dict[listing.state]
    else: 
        state = "No State"
    context = { "listing" : listing, "state": state}  
    return render(request, "listing.html", context) 


@login_required(login_url="/login/") 
def listing_create(request):  # function to create a new listing and add to database. it is using django model forms. 
    form = ListingForm() 
    if request.method == "POST": 
        form = ListingForm(request.POST, request.FILES) 
        if form.is_valid():
            property = form.save() 
            property.user = request.user 
            property.save() 
            data = form.cleaned_data 
            return redirect("/listings/all/")
    context = {"form" : form} 
    return render(request, "listing_create.html", context) 



@login_required(login_url="/login/")
def listing_update(request, pk): # this function is for updating the listing information
    listing = Listing.objects.get(id=pk) 
    form = ListingForm(instance=listing) 
    if request.method == "POST": 
        form = ListingForm(request.POST, request.FILES or None, instance=listing) 
        if form.is_valid(): 
            form.save()
            return redirect("/user/myproperties") 
    context = {"form": form} 
    return render(request, "listing_update.html", context) 


@login_required(login_url="/login/")
def listing_delete(request, pk): # this function is for deleting the listing 
    listing = Listing.objects.get(id=pk) 
    listing.delete() 
    return redirect("/listings/all/")

def listing_rent_list(request):
    rents = Listing_rent.objects.all() 
    context = {"rents": rents}
    return render(request, "listings_rent.html", context)

def listing_rent(request, pk): 
    rent = Listing_rent.objects.get(pk=pk) 
    context = {"rent": rent} 
    return render(request, "listing_rent.html", context) 


