from django.contrib import admin
from .models import Shop
from django.contrib.gis.admin import OSMGeoAdmin

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name','location', 'city',)
# Register your models here.
