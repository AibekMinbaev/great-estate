from django.urls import path 
from .views import login_user, aboutus, contactus_create, profile_page, my_properties, profile_edit


urlpatterns = [
    path('aboutus/', aboutus), 
    path('contactus/', contactus_create), 
    path('login/', login_user),
    path('myprofile/', profile_page),
    path('myprofile/edit/', profile_edit),
    path('myproperties/', my_properties),
] 
