from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp import forms

# Create your views here.
def display(request):
    if request.method=='POST':
        form=forms.empform(request.POST)
        if form.is_valid():
            print('welcome to django validations')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['sal'])
            print(form.cleaned_data['add'])
            print(form.cleaned_data['pno'])
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.empform()

    return render(request,'myapp/welcome.html',{'form':form})
def thank(request):
    return render(request,'myapp/thanks.html')


    return render(request,'myapp/welcome.html',{'form':form})