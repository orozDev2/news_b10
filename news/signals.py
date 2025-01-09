import os
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

from news.models import News, Category


@receiver(post_save, sender=User)
@transaction.atomic()
def post_save_user(sender, instance: User, created, *args, **kwargs):
    if created:
        category, category_created = Category.objects.get_or_create(name='New user')

        news = News.objects.create(
            name=f'New user | {instance.get_full_name()}',
            description=f'New user {instance.get_full_name()} '
                        f'was registered at {instance.date_joined.strftime("%d-%m-%Y")}',
            content='No content',
            category=category,
            author=instance,
        )

        with open(os.path.join(settings.BASE_DIR, 'static', 'static_rs', 'img', 'user.png'), 'rb') as b_img:
            image = File(b_img, f'{instance.username}.png')
            news.image = image
            news.save()

