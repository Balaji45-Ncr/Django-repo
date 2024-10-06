from django.shortcuts import render
from webapp import forms
from django.http import HttpResponseRedirect
# Create your views here.
def display(request):
    if request.method=='POST':
        form=forms.empform(request.POST)
        if form.is_valid():
            print('welcome to validators')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['date'])
            print(form.cleaned_data['opinion'])
            print(form.cleaned_data['sal'])
            print(form.cleaned_data['img'])
            return HttpResponseRedirect('/thanks')
    else:
        form=forms.empform()
    return render(request,'myapp/welcome.html',{'form':form})
def thankyou(request):
    return render(request,'myapp/thanks.html')