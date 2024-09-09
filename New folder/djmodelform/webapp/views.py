from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.forms import empform

# Create your views here.
def thanks(request):
    return render(request,'myapp/thanks.html')

def display(request):
    if request.method=='POST':
        form=empform(request.POST)
        if form.is_valid():
            print("welcome to front end and backend")
            form.save(commit=True)
            return HttpResponseRedirect('/thanks')
    else:
        form=empform()
    return render(request,'myapp/welcome.html',{'form':form})