from django.db import models

# Create your models here.
class Emp(models.Model):
    Empid=models.IntegerField()
    Empname=models.CharField(max_length=255)
    Empnum=models.IntegerField()
    Empsal=models.FloatField()
    Empadd=models.CharField(max_length=100)