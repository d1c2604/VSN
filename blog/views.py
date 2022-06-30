from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fblog(request):
    return render(request,'blog.html')