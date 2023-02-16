from django.shortcuts import render, redirect 
from .models import Listing, Listing_rent 
from .forms import ListingForm 
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users 

# Create your views here.
# CGUD - create, read, update, delete and list(will show all the elements) 



def listing_list(request): # this function will list out all elements in listing database 
    listings = Listing.objects.all() # list of all objects 
    context = { "listings" : listings}
    return render(request, "listings.html", context)  


def listing_retrieve(request, pk): # this function will list a signle element by id 
    listing = Listing.objects.get(id=pk) 
    context = { "listing" : listing}  
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







