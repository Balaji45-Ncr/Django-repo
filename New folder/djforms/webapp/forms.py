from django import forms

class empform(forms.Form):
    name=forms.CharField()
    sal=forms.IntegerField()
    add=forms.CharField()
    number=forms.CharField()