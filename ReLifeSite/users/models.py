import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.deconstruct import deconstructible

from .imageEditor import crop_image


class User(AbstractUser):
    pass


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("img/avatar/")


class Account(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', null=True, blank=True, max_length=32)
    last_name = models.CharField('Фамилия', null=True, blank=True, max_length=32)
    birthday = models.DateField('День рождения', null=True, blank=True, )
    gender = models.CharField(
        'Пол пользователя',
        null=True,
        blank=True,
        max_length=7,
        choices=[
            ('Мужской', 'Мужской'),
            ('Женский', 'Женский')
        ]
    )
    phone = models.CharField('Номер моб. телефона', null=True, blank=True, max_length=10)
    role = models.CharField(
        'Роль пользователя',
        null=True,
        blank=True,
        max_length=25,
        choices=[
            ('Пользователь', 'Пользователь'),
            ('Спонсор', 'Спонсор'),
            ('Ангел', 'Ангел'),
            ('Создатель', 'Создатель'),
        ],
        default='Пользователь'
    )
    accept_ua_pp = models.BooleanField('Согласие со всеми правилами', null=True, blank=True, default=True)
    nick_in_credits = models.CharField('Ник для титров', null=True, blank=True, max_length=64)
    web_site = models.CharField('Веб-сайт', null=True, blank=True, max_length=64)
    github = models.CharField('GitHub', null=True, blank=True, max_length=64)
    telegram = models.CharField('Telegram', null=True, blank=True, max_length=64)
    discord = models.CharField('Discord', null=True, blank=True, max_length=64)
    ip_address = models.CharField('Ip', null=True, blank=True, default='ABC', max_length=64)
    img = models.ImageField('Аватар', null=True, blank=True, upload_to=path_and_rename,
                            default='img/avatar/standard_avatar.png')

    def save(self, **kwargs):
        super().save()
        crop_image(self.img.path)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь_доп'
        verbose_name_plural = 'Пользователи_доп'


class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Идентификатор устройства'
        verbose_name_plural = 'Идентификаторы устройств'


class Nov(models.Model):
    title = models.CharField('Новость', max_length=255)
    description = models.TextField('Описание')
    description_comp = models.CharField('Краткое описание', max_length=255)
    author = models.CharField('Автор', max_length=255)
    date = models.DateField('Дата публикации', auto_now_add=True)
    img = models.ImageField('Превью', null=True, blank=True, upload_to='img/news/')
    link_news = models.CharField('Ссылка', max_length=255)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True, default=0)

    def total_views(self):
        return self.views.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# class Project_cost(models.Model):
#     date = models.DateField('Месяц')
#     cost = models.IntegerField('Цена')
#
#     def __str__(self):
#         return f"Стоимость на {self.date}"
#
#     class Meta:
#         verbose_name = 'Цена'
#         verbose_name_plural = 'Цены'


class Mod(models.Model):
    title = models.CharField('Название мода', max_length=255)
    description = models.TextField('Описание')
    author = models.CharField('Автор', max_length=255)
    date = models.DateField('Дата публикации', auto_now_add=True)
    img_mod = models.ImageField('Превью мода', null=True, blank=True, upload_to='img/mods/')
    mod = models.FileField('Модификация', null=True, blank=True, upload_to='game/modifications/')
    accept_mod = models.BooleanField('Подтверждение', null=True, blank=True, default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Модификация'
        verbose_name_plural = 'Модификации'
