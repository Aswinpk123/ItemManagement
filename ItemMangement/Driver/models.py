from hashlib import blake2b
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.

class DocumentsModel(models.Model):
    docimage = models.ImageField(upload_to='Documents',null=False)
    
    
class DetailsModel(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    prof_image = models.ImageField(upload_to='ProfileImage',null=False)
    Phone = models.CharField(max_length=100,null=False,blank=False)
    vehicle_number = models.CharField(max_length=100,null=False,blank=False,default='')
    referedcommision = models.CharField(max_length=100,null=False,blank=False,default=0)
    drivercommision = models.CharField(max_length=100,null=False,blank=False,default=0)
    documents = models.ManyToManyField(DocumentsModel)
    

    

'''
data

image
1. document object

2. DetailsSerializer(data)
detais -- object
save(document=document_obj)

details_obj.document=document_obj
details_obj.save()
'''