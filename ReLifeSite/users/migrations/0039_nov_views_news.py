# Generated by Django 4.1 on 2022-09-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_alter_account_accept_ua_pp'),
    ]

    operations = [
        migrations.AddField(
            model_name='nov',
            name='views_news',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
