from django import forms
from django.contrib import admin

# Register your models here.
from .models import Trip, Picture, Category, Month, HomeImage, Condition
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)

# admin.site.register(Category)
# admin.site.register(Month)
admin.site.register(Condition)


class PictureAdmin(admin.ModelAdmin):
    list_display = ("trip", "name", "image", "id")


admin.site.register(Picture, PictureAdmin)


class CustomAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(HomeImage, CustomAdmin)


class TripsAdmin(admin.ModelAdmin):
    list_display = ("name", "top_offer", "price", "country", "duration")


admin.site.register(Trip, TripsAdmin)
