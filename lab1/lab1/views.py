from django.shortcuts import render
from django.http.response import HttpResponse

def login(request):
    return HttpResponse("<h1>Log in </h1>")

def register(request):
    return HttpResponse('<h1>Register</h1>')