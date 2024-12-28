import django_filters
from django import forms

from news.models import News, Category, Tag


class NewsFilter(django_filters.FilterSet):
    categories = django_filters.ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple())
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())

    date = django_filters.DateRangeFilter()

    # date_from = django_filters.DateFilter(lookup_expr='gte', field_name='date', label='Дата от')
    # date_to = django_filters.DateFilter(lookup_expr='lte', field_name='date', label='Дата до')

    class Meta:
        model = News
        fields = ('date', 'is_published', 'tags')
