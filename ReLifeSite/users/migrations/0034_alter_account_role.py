# Generated by Django 4.1 on 2022-08-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_alter_account_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(blank=True, choices=[('Пользователь', 'Пользователь'), ('Спонсор', 'Спонсор'), ('Ангел', 'Ангел'), ('Создатель', 'Создатель')], default='Пользователь', max_length=25, null=True, verbose_name='Роль пользователя'),
        ),
    ]
