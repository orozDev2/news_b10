from django import template

from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def news_views(news):
    return sum(item.views for item in news)


@register.filter()
def capitalize(val):
    return val[0].upper() + val[1:]