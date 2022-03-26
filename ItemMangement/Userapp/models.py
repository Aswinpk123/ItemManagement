from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserDetails(AbstractUser):
    mobile = models.CharField(max_length=12,null=False)
    address = models.TextField(null=True,blank=True)
    role = models.CharField(max_length=100,null=True,default='')