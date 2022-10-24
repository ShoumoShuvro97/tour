from django.contrib import admin

# Register your models here.
from accounts.models import Package, Tourist

admin.site.register(Package)
admin.site.register(Tourist)