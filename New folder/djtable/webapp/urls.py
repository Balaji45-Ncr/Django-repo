from django.urls import path
from webapp import views

urlpatterns=[path('home/',views.hello),
             ]