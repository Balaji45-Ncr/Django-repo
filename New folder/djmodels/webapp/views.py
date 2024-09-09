from django.shortcuts import render
from webapp.models import Emp

def display(request):
    Show=Emp.objects.all
    return render(request,'myapp/welcome.html',{'show':Show})