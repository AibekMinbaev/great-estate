from django.urls import path  
from .views import messages_page, messages_detail

urlpatterns = [
    path('messages/', messages_page),
    path('message/<pk>/', messages_detail),
]