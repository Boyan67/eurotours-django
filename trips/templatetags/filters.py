from django import template
from django.forms import CheckboxInput

register = template.Library()


@register.filter
def category_in(category_id, category_list):
    return category_list.filter(id=category_id).exists()


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__
