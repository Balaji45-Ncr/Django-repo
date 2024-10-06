from django.contrib import admin
from webapp.models import empnames
# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['name','salary','address','number']
admin.site.register(empnames,empadmin)