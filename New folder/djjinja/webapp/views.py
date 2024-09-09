from django.shortcuts import render
import datetime

# Create your views here.
def hello(request):
    s=datetime.datetime.now()
    name='Balaji'
    th=int(s.strftime("%H"))
    if th<=10:
        wish="welcome to morning life"
    elif th<=15:
        wish="welcome to afternoon&night life"
    else:
        wish="welcome to night life buddy"
    return render(request,'myapp/welcome.html',{'s':s,'name':name,'wish':wish})
