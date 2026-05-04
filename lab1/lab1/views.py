from django.shortcuts import render
from django.http.response import HttpResponse

def login(request):
    return render(request,'login/login.html')

def register(request):
    return render(request,'register/register.html')