from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def aboutus(request):
    return HttpResponse("<h1>About Us Page</h1>")

def contactus(request):
    return HttpResponse("<h1>Contact Us Page </h1>")
