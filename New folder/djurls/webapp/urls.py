from django.contrib import admin
from django.urls import path,re_path,include
from webapp import views

urlpatterns=[path('home/<int:year>',views.inner),
             ]