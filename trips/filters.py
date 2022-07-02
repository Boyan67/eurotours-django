import django_filters
from django import forms

from django_filters import RangeFilter, NumericRangeFilter

from .models import *


class TripFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label="От:")
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label="До:")
    country = django_filters.filters.AllValuesFilter()
    months = django_filters.filters.ModelChoiceFilter(queryset=Month.objects.all())

    # conjoined=True - to use AND instead of OR
    # category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
    #                                                     widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Trip
        fields = ['text', 'months']