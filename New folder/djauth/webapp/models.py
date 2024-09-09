from django.db import models

# Create your models here.
class empnames(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    address=models.CharField(max_length=50)
    number= models.IntegerField()
