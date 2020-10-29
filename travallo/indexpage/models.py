from django.db import models

# Create your models here.


class Destination(models.Model):
    name =  models.CharField(max_length=260)
    discription =  models.TextField()
    price =  models.IntegerField()
    img =  models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)

    
