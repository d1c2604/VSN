from django.urls import path 
from blog.views import *


urlpatterns = [
    path('',fblog,name='blog function'),
   
]
