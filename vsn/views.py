from http.client import ImproperConnectionState
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')