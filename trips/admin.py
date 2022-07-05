from django import forms
from django.contrib import admin

# Register your models here.
from .models import Trip, Picture, Category, Month, HomeImage, Condition
from django.contrib.auth.models import User
from django.contrib.auth.models import Group





# `admin.site.unregister(User)
admin.site.unregister(Group)

# admin.site.register(Category)
# admin.site.register(Month)
admin.site.register(Condition)


class PictureAdmin(admin.ModelAdmin):
    list_display = ("trip", "name", "image", "id")
    search_fields = ("name",)
    list_filter = ("trip",)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PictureAdmin, self).get_search_results(request, queryset, search_term)
        try:

            ids = []
            for i in Picture.objects.all():
                if search_term.lower() in i.trip.name.lower():
                    ids.append(i.id)
            queryset |= self.model.objects.filter(pk__in=ids)
        except:
            print("\n==========\n===========\nERROR in admin.py get_search_result")

        return queryset, use_distinct


admin.site.register(Picture, PictureAdmin)


class CustomAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(HomeImage, CustomAdmin)


class TripsAdmin(admin.ModelAdmin):
    list_display = ("name", "top_offer", "price", "country", "duration")
    list_filter = ("top_offer", "category", "months", "country", "duration", "category")
    search_fields = ("name",)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(TripsAdmin, self).get_search_results(request, queryset, search_term)
        if search_term != "":
            try:
                ids = []
                for i in Trip.objects.all():
                    if search_term.lower() in i.name.lower():
                        ids.append(i.id)
                queryset |= self.model.objects.filter(pk__in=ids)

            except:
                print("\n==========\n===========\nERROR in admin.py TripsAdmin get_search_results")
        return queryset, use_distinct






admin.site.register(Trip, TripsAdmin)
