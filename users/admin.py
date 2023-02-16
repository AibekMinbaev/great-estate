from django.contrib import admin
from .models import ContactUs, My_profile

admin.site.register(ContactUs)  
admin.site.register(My_profile) 
admin.site.site_url = "/home/"  

