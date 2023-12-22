from contextvars import Token
from django.contrib.auth import authenticate,login
from rest_framework import generics
from django import views
from django.shortcuts import render
from h11 import Response
from Usermodule_app.models import shortenedURl
from Usermodule_app.serializers import Userserializers, shortURLSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

class userRegistraionview(generics.CreateAPIView):
    serializer_class=Userserializers


    def create(self,request,*args,**kwargs):
        serilizer=self.get_serilizer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        user=serilizer.save()
        Token.objects.create(user=user)
        return Response({"token":user.auth_token.key},status=status.HTTP_201_CREATED)
    
class Userloginview(views.APIView):
    def post(self,request,*args,**kwargs):
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(request,email=email,password=password)

        if user:
            login(request,user)
            return Response({"message:login successful"})
        else:
            return Response({"message:login unsuccessful"})    

class createShorturlview(generics.createApiView):
    serializer_class=shortURLSerializer
    Permission_classes=[IsAuthenticated]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class shortURLDetailsview(generics.retrieveupdatedestroyAPIview):
    queryset=shortenedURl.objects.all()
    serializer_class=shortURLSerializer
    Permission_classes=[IsAuthenticated]


class userLogoutview(APIView):
    permisissiom_classes=[IsAuthenticated]
    def poist (self,request):
        request.auth.dete()
        return Response({"message:logout successful"},status==status.HTTP_200_ok)