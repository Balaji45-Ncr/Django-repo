from django import forms
from webapp.models import emp

class empform(forms.ModelForm):
    class Meta():
        model=emp
        fields='__all__'