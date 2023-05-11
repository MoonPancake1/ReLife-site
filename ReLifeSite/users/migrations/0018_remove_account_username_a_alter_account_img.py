# Generated by Django 4.1 on 2022-08-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_account_username_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username_a',
        ),
        migrations.AlterField(
            model_name='account',
            name='img',
            field=models.ImageField(blank=True, default='avatar/standard_avatar.png', null=True, upload_to='avatar/', verbose_name='Аватар'),
        ),
    ]