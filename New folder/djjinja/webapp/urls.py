from django.urls import path,re_path
from webapp import views
urlpatterns=[path('home/',views.hello)]