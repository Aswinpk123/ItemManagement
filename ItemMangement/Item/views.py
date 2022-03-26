from functools import partial
import django
from django.shortcuts import render
from ItemMangement.Constants import *
from Userapp.serializers import UserSerializer
from Userapp.models import UserDetails
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class ItemTypeAPI(ListAPIView):
    serializer_class = ItemTypeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        if serializer.data['role'] == "Admin":
            id = self.request.POST.get("id","")

            if id:
                itype = ItemTypeModel.objects.filter(id = id)
                if itype.count():
                    modifydata = itype.first()
                    data = ItemTypeSerializer(modifydata,data=self.request.data,partial=True)
                    msg = "Updated Successfully" 
                else:
                    return Response({ STATUS:False, MESSAGE:"No record found with the id" })
            else:
                data = ItemTypeSerializer(data = self.request.data)
                msg = "Created Succesfully"

            data.is_valid(raise_exception=True)
            saved = data.save()
            saveddata = ItemTypeSerializer(saved).data            
            return Response({
                STATUS : True,
                MESSAGE : msg,
                RESULT : saveddata
            })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admin can do this operation"
            })

    def get_queryset(self):
        
        id = self.request.POST.get("id","")
        name = self.request.POST.get("Typename","")

       
        data = ItemTypeModel.objects.all()

        if id:
            data = data.filter(id=id)

        if name:
            data = data.filter(Typename__icontains = name)     
       
        return data

    def delete(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        print("Roleeeee",serializer.data)
        if serializer.data['role'] == "Admin":
            id = self.request.POST.get("id","")
            if id:
                itype = ItemTypeModel.objects.filter(id = id)
                if itype.count():
                    modifydata = itype.first()
                    modifydata.delete()
                    return Response({
                        STATUS : True,
                        MESSAGE : "Date Deleted Succesfully",

                        })
                else:
                    return Response({ STATUS:False, MESSAGE:"No record found with the id" })
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : "Please Provide an Id",
                    
                })
        else:
            return Response({
                STATUS : False,
                MESSAGE :"only admins can do this operation"
            })



class ItemAPI(ListAPIView):
    serializer_class = ItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        print("Roleeeee",serializer.data)
        if serializer.data['role'] == "Admin":
            id = self.request.POST.get("id","")

            if id:
                itype = ItemModel.objects.filter(id = id)
                if itype.count():
                    modifydata = itype.first()
                    data = ItemSerializer(modifydata,data=self.request.data,partial=True)
                    msg = "Updated Successfully" 
                else:
                    return Response({ STATUS:False, MESSAGE:"No record found with the id" })
            else:
                data = ItemSerializer(data = self.request.data)
                msg = "Created Succesfully"

            data.is_valid(raise_exception=True)
            saved = data.save()
            saveddata = ItemSerializer(saved).data            
            return Response({
                STATUS : True,
                MESSAGE : msg,
                RESULT : saveddata
            })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admin can do this operation"
            })

    def get_queryset(self):

        id = self.request.POST.get("id","")
        name = self.request.POST.get("Itemname","")

        data = ItemModel.objects.all()
        if id:
            data = data.filter(id=id)
        if name:
            data = data.filter(Itemname__icontains = name)
        return data

    def delete(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        print("Roleeeee",serializer.data)
        if serializer.data['role'] == "Admin":
            id = self.request.POST.get("id","")
            if id:
                itype = ItemModel.objects.filter(id = id)
                if itype.count():
                    modifydata = itype.first()
                    modifydata.delete()
                    return Response({
                        STATUS : True,
                        MESSAGE : "Date Deleted Succesfully",

                        })
                else:
                    return Response({ STATUS:False, MESSAGE:"No record found with the id" })
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : "Please Provide an Id",
                    
                })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admins can do this operations"
            })
