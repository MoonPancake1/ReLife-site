# Generated by Django 4.1 on 2022-08-27 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_users_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь_доп', 'verbose_name_plural': 'Пользователи_доп'},
        ),
    ]
