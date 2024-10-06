from django.shortcuts import render
from webapp import forms

# Create your views here.
def home(request):
    show=forms.empform()
    return render(request,'myapp/welcome.html',{'show':show})