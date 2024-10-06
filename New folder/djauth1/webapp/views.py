from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')
@login_required()
def customer(request):
    return render(request,'myapp/cust.html')
def logout(request):
    return render(request,'myapp/logout.html')
