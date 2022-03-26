from functools import partial
from ItemMangement.Constants import *
from ItemMangement.Checking_Function import Checking
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from Userapp.models import *
from Userapp.serializers import *


from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

class DetailsAPI(ListAPIView):
    serializer_class = DetailsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def post(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        if serializer.data['role'] == "Admin":

            id = self.request.POST.get("id","")
    
            if id :          
                if id.isdigit():
                    itype = DetailsModel.objects.filter(id = id)
                    if itype.count():
                        modifydata = itype.first()
                        data = DetailsSerializer(modifydata,data=self.request.data,partial=True)
                        data.is_valid(raise_exception=True)
                        data.save()
                        return Response({ STATUS:True, MESSAGE:"Succesfully Updated" })
                    else:
                        return Response({ STATUS:False, MESSAGE:"No record found with the id" })

                    
                else:
                    return Response({ STATUS:False, MESSAGE:"Please Procide Valid id" })

            else:
                mandatory = ['name','prof_image','Phone','vehicle_number']
                data = Checking(self.request.data,mandatory)

                if data == True:
                    k = []
                    for x in self.request.FILES.getlist('docimage'):
                        doc = DocumentSerializer(data={'docimage':x})
                        doc.is_valid(raise_exception=True)
                        saved = doc.save()
                        saveddata = DocumentSerializer(saved).data   
                        k.append(saveddata['id'])

                    Dt = DetailsSerializer(data=self.request.data,partial=True)
                    Dt.is_valid(raise_exception=True)
                    dats  = Dt.save()
                    dats.documents.add(*k)
                    return Response({
                        STATUS : True,
                        MESSAGE : "Driver Details Succesfully Created"
                    })

                else:
                    return Response({
                        STATUS : False,
                        MESSAGE : data
                    })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admin Can Do this Operation"
            })

    def get_queryset(self):
        data = DetailsModel.objects.all()
        return data

    def delete(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        if serializer.data['role'] == "Admin":
            id = self.request.POST.get("id","")
            if id:
                if id.isdigit():
                    itype = DetailsModel.objects.filter(id = id)
                    if itype.count():
                        modifydata = itype.first()
                        modifydata.documents.all().delete()
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
                        MESSAGE : "Please Provide Valid Id"
                    })
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : "Please Provide an Id",
                    
                })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admin can do this operation"
            })

class DocumetsAPI(ListAPIView):
    serializer_class = DetailsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


    serializer_class = DocumentSerializer
    def get_queryset(self):
        data = DocumentsModel.objects.all()
        return data


    def post(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        if serializer.data['role'] == "Admin":
            driverid = self.request.POST.get("Driverid")
            mandatory = ['Driverid','docimage']
            data = Checking(self.request.data,mandatory)

            if data == True:
                if driverid and driverid.isdigit():
                    driver = DetailsModel.objects.filter(id=driverid)
                    if driver.count():
                        data = driver.first()
                        k = []
                        for x in self.request.FILES.getlist('docimage'):
                            doc = DocumentSerializer(data={'docimage':x})
                            doc.is_valid(raise_exception=True)
                            saved = doc.save()
                            saveddata = DocumentSerializer(saved).data   
                            k.append(saveddata['id'])

                        data.documents.add(*k)
                        return Response({
                            STATUS : True,
                            MESSAGE : "Documents Succesfully Added"
                        })

                    else:
                        return Response({
                            STATUS : False,
                            MESSAGE : "Please Provide Valid Driver ID"
                        })
                else:
                    return Response({
                        STATUS:False,
                        MESSAGE : "Please Provide Valid DriverID"
                    })
                
            
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : data
                })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admins can do this operation"
            })

    def put(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        if serializer.data['role'] == "Admin":
            docid = self.request.POST.get("docid","")
            if docid:
                if docid.isdigit():
                    doc  = DocumentsModel.objects.filter(id=docid)
                    if doc.count():
                        modifydoc  = doc.first()
                        data = DocumentSerializer(modifydoc,data=self.request.data,partial=True)
                        data.is_valid(raise_exception=True)
                        data.save()
                        return Response({
                            STATUS:True, MESSAGE:"Document Succesfully Updated"
                        })
                    else:
                        return Response({
                            STATUS:False, MESSAGE:"No record found with the id"
                        })
                else:
                    return Response({
                        STATUS : False,
                        MESSAGE : "Provide Valid ID"
                })
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : "Provide Valid ID"
                })
        else:
            return Response(
                {
                    STATUS : False,
                    MESSAGE : "Only Admins can do this operation"
                }
            )

    def delete(self,request):
        userrole = UserDetails.objects.get(id=self.request.user.id)
        serializer = UserSerializer(userrole)
        if serializer.data['role'] == "Admin":
            docid = self.request.POST.get("docid","")
            if docid:
                if docid.isdigit():
                    doc  = DocumentsModel.objects.filter(id=docid)
                    if doc.count():
                        doc.first().delete()
                        return Response({
                            STATUS:True, MESSAGE:"Document Deleted Succesfully"
                        })
                    else:
                        return Response({
                            STATUS:False, MESSAGE:"No record found with the id"
                        })
                else:
                    return Response({
                        STATUS : False,
                        MESSAGE : "Provide Valid ID"
                })
            else:
                return Response({
                    STATUS : False,
                    MESSAGE : "Provide Valid ID"
                })
        else:
            return Response({
                STATUS : False,
                MESSAGE : "Only Admins can do this Operation"
            })