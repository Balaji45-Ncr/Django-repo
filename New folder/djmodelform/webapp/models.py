from django.db import models

# Create your models here.
class emp(models.Model):
    name= models.CharField(max_length=100)
    sal = models.IntegerField()
    add = models.CharField(max_length=5)
    img = models.ImageField()
    num = models.IntegerField()
