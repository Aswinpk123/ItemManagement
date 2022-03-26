from ItemMangement.Constants import *
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

# Create your views here.

class ChargesAPI(ListAPIView):
    serializer_class  = ChargeSerializer
    def post(self,request):
        key = self.request.POST.get("key","")
        if key:
            charge = ChargesModel.objects.filter(keyvalue=key)
            if charge.count():
                modify = charge.first()
                data  = ChargeSerializer(modify,data=self.request.data,partial=True)
                msg = "Succesfully Updated"
            else:
                return Response({STATUS : False,MESSAGE:"No data found"})

        else:
            data = ChargeSerializer(data=self.request.data)
            msg = "Succesfully Created"

        data.is_valid(raise_exception=True)
        data.save()

        
        return Response({
            STATUS : True,
            MESSAGE : msg
        })

    def get_queryset(self):
        data = ChargesModel.objects.all()
        return data

    def delete(self,request):
        key = self.request.POST.get("key","")
        if key:
            charge = ChargesModel.objects.filter(keyvalue=key)
            if charge.count():
                modify = charge.first().delete
                return Response({
                    STATUS : True,
                    MESSAGE : "Succesfully Deleted"
                })
            else:
                return Response({STATUS : False,MESSAGE:"No data found"})

        else:
           return Response({
               STATUS : False,
               MESSAGE : "PLease provide a valid key"
           })