from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
# def login(request):
#     if request.method == 'POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')

#         log=Login.objects.get('email','password')
#     return render(request,'login.html')    

class loginregister(generics.ListAPIView,generics.CreateAPIView):
    queryset=Login.objects.all()
    serializer_class = DemoSerial

        

class Logingeneric(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Login.objects.all()
    serializer_class = DemoSerial
    lookup_field='email'