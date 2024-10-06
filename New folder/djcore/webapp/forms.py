from django import forms
from django.core.validators import validate_email
from django.core.exceptions import validationError
from django.core import validators

class empform(forms.Form):
    name=forms.CharField(validators=[RegexValidator])
