from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='название', max_length=100, unique=True)

    def __str__(self):
        return f'{self.id}. {self.name}'


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    name = models.CharField(verbose_name='название', max_length=100, unique=True)

    def __str__(self):
        return f'{self.id}. {self.name}'


class NewsLink(models.Model):
    class Meta:
        verbose_name = 'ссылки новостя'
        verbose_name_plural = 'ссылки новостей'

    news = models.OneToOneField('news.News', on_delete=models.CASCADE, related_name='link', verbose_name='новость')
    instagram = models.URLField(verbose_name='instagram ссылка', null=True, blank=True)
    facebook = models.URLField(verbose_name='facebook ссылка', null=True, blank=True)
    whatsapp = models.URLField(verbose_name='whatsapp ссылка', null=True, blank=True)
    telegram = models.URLField(verbose_name='telegram ссылка', null=True, blank=True)

    def __str__(self):
        return f'{self.news.name}'

    def get_name(self, exp):
        return f'{self.news.name}{exp}'

    def clean(self):

        fields = [
            'instagram',
            'facebook',
            'whatsapp',
            'telegram',
        ]

        # self.instagram = 'dsfsd' #  setattr(self, 'instagram', 'dsfsd')
        # self.save()

        everyNone = True

        for field in fields:
            if getattr(self, field) is not None:
                everyNone = False
                break

        if everyNone:
            raise ValidationError('Пожалуйста, введите хотя бы одно из полей')


def min_max_length(val):
    if 100 > len(val):
        raise ValidationError('Количество символов должно быть больше 99.')

    if 2000 < len(val):
        raise ValidationError('Количество символов должно быть меньше или равно 2000.')

    return val


class News(models.Model):
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    name = models.CharField(verbose_name='название', max_length=100)
    image = models.ImageField(verbose_name='изображение', upload_to='news_images/', )
    description = models.CharField(verbose_name='описание', max_length=300)
    content = models.TextField(verbose_name='контент', validators=[min_max_length])
    date = models.DateTimeField(verbose_name='дата публикации', auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name='дата изменении', auto_now=True)
    # author = models.CharField(verbose_name='автор', max_length=100, null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='news', verbose_name='автор',
                               null=True)
    category = models.ForeignKey('news.Category', on_delete=models.CASCADE, related_name='news', null=True,
                                 verbose_name='категория')
    tags = models.ManyToManyField('news.Tag', related_name='news', verbose_name='теги')
    views = models.PositiveIntegerField(verbose_name='просмотры', default=0,
                                        validators=[MinValueValidator(0)])
    is_published = models.BooleanField(verbose_name='публичный', default=True)

    def __str__(self):
        return f'{self.id}) {self.name}'

    # def clean(self):
    #     if self.id is None:
    #         ...
    #     else:
    #         ...

# Create your models here.
