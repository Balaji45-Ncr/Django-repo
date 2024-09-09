from django import forms
from django.core import validators
from datetime import datetime


class empform(forms.Form):
    name=forms.CharField()
    date=forms.DateTimeField()
    opinion=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(50),validators.MinLengthValidator(5)])
    sal=forms.EmailField()
    img=forms.ImageField(max_length=40,allow_empty_file= True)