from http.client import ImproperConnectionState
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        uid = request.POST['uid']
        mail = request.POST['mail']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        log_stat = False
        

        return render(request,'index.html',{})
    
    else:
        return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')