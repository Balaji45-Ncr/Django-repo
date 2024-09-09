from django.contrib import admin
from webapp.models import Emp

# Register your models here.
class Empadmin(admin.ModelAdmin):
    list_display = ['Empid','Empname','Empnum','Empsal','Empadd']
admin.site.register(Emp)