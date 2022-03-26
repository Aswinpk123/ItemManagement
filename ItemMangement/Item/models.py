from django.db import models

# Create your models here.

class ItemTypeModel(models.Model):
    Typename = models.CharField(max_length=100,null=False,blank=False)
    Price = models.CharField(max_length=100,null=False,blank=False)
    Created_Date = models.DateField(auto_now_add=True)

class ItemModel(models.Model):
    Itemname = models.CharField(max_length=100,null=False,blank=False)
    Itemdesc = models.CharField(max_length=100,null=False,blank=False)
    Created_Date = models.DateField(auto_now_add=True)
    