from django.contrib import admin
from webapp.models import emp

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display = ['name','sal','add','num']
admin.site.register(emp,empadmin)