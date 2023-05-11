# Generated by Django 4.1 on 2022-08-27 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_account_username_a_alter_account_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='discord',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Discord'),
        ),
        migrations.AddField(
            model_name='account',
            name='github',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='GitHub'),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=10, null=True, verbose_name='Номер моб. телефона'),
        ),
        migrations.AddField(
            model_name='account',
            name='role',
            field=models.CharField(blank=True, choices=[('Пользователь', 'Пользователь'), ('Спонсор', 'Спонсор'), ('Создатель', 'Создатель')], max_length=25, null=True, verbose_name='Роль пользователя'),
        ),
        migrations.AddField(
            model_name='account',
            name='telegram',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Telegram'),
        ),
        migrations.AddField(
            model_name='account',
            name='web_site',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Веб-сайт'),
        ),
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=7, null=True, verbose_name='Пол пользователя'),
        ),
    ]
