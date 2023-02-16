from django.contrib import admin
from django.urls import path, include 
from listings.views import listing_list, listing_retrieve, listing_create, listing_update, listing_delete, listing_rent_list, listing_rent
from .views import home_view 
from users.views import register, login_user, logout_user 

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/logout/', logout_user),
    path('admin/', admin.site.urls),

    path('register/',register), 
    path('login/',login_user),
    path('logout/', logout_user), 


    path("home/", home_view), 
    path('listings/all/', listing_list),
    path('listings/single/<pk>/',listing_retrieve ),
    path('listings/create/', listing_create), 
    path('listings/single/<pk>/update/', listing_update),
    path('listings/single/<pk>/delete/', listing_delete), 
    path('rent/all/', listing_rent_list), 
    path('rent/single/<pk>/', listing_rent), 

    path('user/', include('users.urls')),
    path('staff/', include('staff.urls'))  
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


      