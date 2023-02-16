from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib import messages 
from .forms import ContactUsForm, FormUserCreation, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.forms import UserChangeForm 
from .models import My_profile
from listings.models import Listing 

def contactus_create(request):  
    form = ContactUsForm() 
    if request.method == "POST": 
        form = ContactUsForm(request.POST) 
        if form.is_valid(): 
            form.save()  
            messages.success(request, "Your message was send successfully")
            return redirect("/user/contactus/")
    context = {"form" : form}
    return render(request, "user_contactus.html", context) 

def aboutus(request): 
    return render(request, "aboutus.html") 

@unauthenticated_user
def register(request): 
    form = FormUserCreation() 
    if request.method == "POST":  
        form = FormUserCreation(request.POST) 
        if form.is_valid():
            form.save()
            user = form.save() #What is going on here 
            group = Group.objects.get(name='customers') 
            group.user_set.add(user) # adding the user to the group 

            username = form.cleaned_data.get("username")
            messages.success(request, "Successfully created an account for " + username) 
            return redirect("/login/")
    context = {"form" : form} 
    return render(request, "register.html", context)

@unauthenticated_user
def login_user(request):
    if request.method == "POST":  
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = None 
            if request.user.groups.exists(): 
                group = request.user.groups.all()[0].name
                if group == 'admins': 
                    return redirect("/admin/")  # if the user is admin send him to admin panel
            return redirect("/home/") 
        else:
            messages.info(request,"Username or Password is incorrect")
    context = {}
    return render(request, "registration/login.html", context) 


def logout_user(request): 
    logout(request) 
    return redirect("/home/")


@login_required(login_url="/login/") 
def my_profile(request): 
    return render(request, "myprofile.html")  

@login_required(login_url="/login/") 
@allowed_users(allowed_roles=['customers'])
def my_properties(request): 
    listings = Listing.objects.filter(user=request.user) 
    context = {"listings":listings}
    return render(request, "myproperties.html", context) 

@login_required(login_url="/login/") 
def profile_page(request): 
    user = request.user 
    try: 
        profile = user.my_profile 
    except My_profile.DoesNotExist: 
        profile = My_profile.objects.create(user=user)

    print(vars(profile)) 
    if profile.profile_pic == "": 
        profile.profile_pic = 'default.png'
        profile.save()
    context = {'user':user, 'profile':profile} 
    return render(request, 'myprofile.html', context)  


@login_required(login_url="/login/") 
def profile_edit(request): 
    profile = request.user.my_profile
    if request.method == "POST": 
        form = CustomUserChangeForm(request.POST,request.FILES or None, instance=request.user) 
        if form.is_valid(): 
            user = form.save()
            profile.age = form.cleaned_data['age'] 
            profile.phone_number = form.cleaned_data['phone_number']
            if form.cleaned_data['profile_pic'] != None: 
                profile.profile_pic = form.cleaned_data['profile_pic'] # this is not working I think 
            profile.save()
            return redirect('/user/myprofile/')   # this function is deleting when submit 
    else: 
        print(vars(profile)) 
        print("get")
        form = CustomUserChangeForm(instance=request.user, initial={'profile_pic': request.user.my_profile.profile_pic, 'age': request.user.my_profile.age, 'phone_number': request.user.my_profile.phone_number}) 
    context = {'form': form}
    return render(request, 'profile_edit.html', context) 