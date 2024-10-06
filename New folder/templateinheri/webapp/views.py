from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
def news(request):
    return render(request,'myapp/news.html')
def sports(request):
    return render(request,'myapp/sports.html')