# Generated by Django 4.1 on 2022-08-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_users_alter_nov_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
