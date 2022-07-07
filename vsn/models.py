from django.db import models

class User(models.Model):
    uname = models.CharField(max_length=20,blank=False)
    uid = models.CharField(max_length=10, blank = False)
    phone = models.IntegerField(max_length=10)
    mail = models.EmailField(blank=True)
    pawd = models.TextField(blank=False)
    bg = models.ImageField(blank = True)


    