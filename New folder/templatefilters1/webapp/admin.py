from django.contrib import admin
from webapp.models import filtering

class filteradmin(admin.ModelAdmin):
    list_display=['name','age','address','salary']
admin.site.register(filtering,filteradmin)

