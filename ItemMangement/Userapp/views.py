from multiprocessing import context
from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from django.contrib.auth.hashers import make_password
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly



# Create your views here.

class UserAPI(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        id = self.request.POST.get("id","")
        username = self.request.POST.get("username","")
        datas = UserDetails.objects.all()
        if id:
            datas = datas.filter(id=id)
        if username:
            datas = datas.filter(username__icontains = username)
        return datas


    def post(self, request):
        user_obj = ""
        print("Receved User data ",self.request.data)

        try:
            id = self.request.POST.get("id", "")
            if id:
                user_qs = UserDetails.objects.filter(id=id)
                serializer = UserSerializer(user_qs.first(),data=request.data,partial=True)
                serializer.is_valid(raise_exception=True)

                password = self.request.POST.get('password','')
                if password :
                    msg="User details and password updated"
                    user_obj = serializer.save(password=make_password(password))
                else:
                    msg="User details updated"
                    user_obj = serializer.save()
            else:
                print("Adding new UserDetails")
                serializer = UserSerializer(data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
               
                msg = "Created New User"
                user_obj = serializer.save(password=make_password(self.request.data['password']))

            return Response({
                "Status":True,
                "Message":msg
            })

        except Exception as e:
            print(f"Excepction occured {e}")

            if user_obj:
                user_obj.delete()

            return  Response({
                "Status":False,
                "Message":f"Excepction occured {e}"
            })

class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        
        print(serializer)
        try:
            test = serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            print("user pk",user.pk)
            print("user id",user.id)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "STATUS":True,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
            })
        except Exception as e:
            return Response({
                "STATUS":False,
                "MESSAGE":"Incorrect Username or Password",
                "excepction":str(e),
            })

class WhoAmI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        print("UUUUUUUUUUUUUUUUUUU",self.request.user.id)
        datas = UserDetails.objects.get(id=self.request.user.id)
        serializer =  UserSerializer(datas)
        # serializer.is_valid(raise_exception=True)
        return Response({
            "Status":1,
            "Data":serializer.data
        })

class Logout(ListAPIView):
   
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        datas = Token.objects.get(user=self.request.user.id)
        datas.delete()
        # serializer.is_valid(raise_exception=True)
        return Response({
            "Status":True,
            "Data":"Succesfully Logout"
        })