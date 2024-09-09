from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import request
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
@login_required()
def cust(request):
    return render(request,'myapp/cust.html')
def logout(request):
    return render(request,'myapp/logout.html')

def signup(request):
     if request.method=='POST':
         form=UserCreationForm(request.POST)
         if form.is_valid():
             form.save(commit=True)
             return redirect('/')
     else:
         form=UserCreationForm()
     return render(request,'myapp/logout.html',{'form':form})
