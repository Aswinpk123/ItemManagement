from operator import mod
from turtle import ondrag
from django.db import models
from Driver.models import DetailsModel
from Item.models import ItemTypeModel,ItemModel
# Create your models here.




class JobModels(models.Model):
    jobname = models.CharField(max_length=100,null=False,blank=False)
    fromplace = models.CharField(max_length=100,null=False,blank=False)
    toplace = models.CharField(max_length=100,null=False,blank=False)
    totalkm = models.CharField(max_length=100,null=False,blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    customername = models.CharField(max_length=100,null=False,blank=False)
    customerphone = models.CharField(max_length=100,null=False,blank=False)
    assigneddriver = models.ForeignKey(DetailsModel,related_name='drname',on_delete=models.DO_NOTHING)
    itemname = models.ForeignKey(ItemModel,on_delete=models.DO_NOTHING)
    itemtype = models.ForeignKey(ItemTypeModel,on_delete=models.DO_NOTHING)
    transfercharge = models.CharField(max_length=100,null=False,blank=False)
    extracharge = models.CharField(max_length=100,null=False,blank=False)
    drivercommision = models.CharField(max_length=100,null=False,blank=False,default=0)
    referercommision = models.CharField(max_length=100,null=False,blank=False,default=0)
    labourcharge = models.CharField(max_length=100,null=False,blank=False)
    jobrefered = models.ForeignKey(DetailsModel,on_delete=models.DO_NOTHING,null=True)
    Total = models.CharField(max_length=100,null=False,blank=False,default=0)
    jobstatus = models.CharField(max_length=100)
