
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('blog',include('blog.urls')),
    path('contact',contact,name='contact_page'),
    path('media',include('media.urls')),
    
]
