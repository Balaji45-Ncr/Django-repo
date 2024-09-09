from django.shortcuts import render

# Create your views here.
from webapp import models

def empclass(request):
    list_all=models.emp.objects.all()
    return render(request,'myapp/welcome.html',{'list':list_all})
