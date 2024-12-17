from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, Category, Tag, NewsLink

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(NewsLink)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'category', 'author', 'is_published', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = (
        'name',
        'description',
        'content',
        'author',
        'category__name',
        'tags__name',
    )
    list_filter = ('category', 'tags', 'date', 'is_published')
    list_editable = ('is_published',)
    readonly_fields = ('views', 'date', 'last_updated', 'get_full_image')

    @admin.display(description='Изображение')
    def get_image(self, news):
        return mark_safe(f'<img src="{news.image.url}" width="100px">')

    @admin.display(description='Изображение')
    def get_full_image(self, news):
        return mark_safe(f'<img src="{news.image.url}" width="75%">')

# admin.site.register(News, NewsAdmin)

# Register your models here.
