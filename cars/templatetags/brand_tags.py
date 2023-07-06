from django import template
from cars.models import Brand

register = template.Library()


@register.simple_tag()
def get_brands():
    return Brand.objects.all()
