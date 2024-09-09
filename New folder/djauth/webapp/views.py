from django.shortcuts import render
from webapp.models import empnames
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'myapp/welcome.html')
def customer(request):
    return render(request,'myapp/cust.html')