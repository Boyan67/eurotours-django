from django.contrib import admin

# Register your models here.
from .models import Trip, Image, Category, Month

admin.site.register(Trip)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Month)