from django.contrib import admin
from webapp.models  import emp
# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['name','add']
admin.site.register(emp,empadmin)