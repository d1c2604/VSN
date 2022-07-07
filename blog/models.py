from django.db import models




class blog(models.Model):
    uid = models.CharField( max_length=20)
    title = models.CharField( max_length=30)
    dop = models.DateField(blank=True)
    likes = models.IntegerField(default=0)
    
    

