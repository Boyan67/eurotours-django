from django.contrib import admin

# Register your models here.
from .models import Trip, Picture, Category, Month

admin.site.register(Trip)
admin.site.register(Picture)
admin.site.register(Category)
admin.site.register(Month)