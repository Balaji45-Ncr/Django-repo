from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def outer(request):
    return HttpResponse("Welcome to home")
def inner(request,year):
    return HttpResponse(f"Welcome to year {year}")
