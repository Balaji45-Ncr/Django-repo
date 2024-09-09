from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello <a href="/Hello">Hello1</a></h1>')

def reply(request):
    return HttpResponse('Bye!')
