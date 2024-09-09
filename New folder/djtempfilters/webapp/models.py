from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=30)
    add=models.CharField(max_length=40)
    sal=models.IntegerField()
    date=models.DateField()
