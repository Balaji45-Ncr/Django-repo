from django.shortcuts import render
from webapp.models import filtering

# Create your views here.
def display(request):
    name=filtering.objects.all()
    return render(request,'myfile/home.html',{'name':name})
