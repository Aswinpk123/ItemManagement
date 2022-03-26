from operator import mod
from django.db import models

# Create your models here.

class ChargesModel(models.Model):
    perkmcharge = models.CharField(max_length=100)
    extracharge = models.CharField(max_length=100)
    extradescription = models.CharField(max_length=100)
    referorcommision = models.CharField(max_length=100)
    drivercommision = models.CharField(max_length=100)
    keyvalue = models.CharField(max_length=100,default=1)