from django.shortcuts import render


# Create your views here.
def mytemplates(request):
    return render(request,'myapp/welcome.html')