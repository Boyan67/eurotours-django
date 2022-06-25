from django import template

register = template.Library()


@register.filter
def category_in(category_id, category_list):
    return category_list.filter(id=category_id).exists()
