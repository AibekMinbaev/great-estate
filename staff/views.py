from django.shortcuts import render
from users.decorators import unauthenticated_user, allowed_users
from users.models import ContactUs 



@allowed_users(allowed_roles=['admins','staffs'])
def messages_page(request): 
    messages = ContactUs.objects.all()
    context = {'messages': messages}
    return render(request, 'messages_page.html', context)  


@allowed_users(allowed_roles=['admins','staffs'])
def messages_detail(request, pk): 
    message_detail = ContactUs.objects.get(pk=pk) 
    context = {'message_detail' : message_detail} 
    return render(request, 'message_detail.html', context) 
    
