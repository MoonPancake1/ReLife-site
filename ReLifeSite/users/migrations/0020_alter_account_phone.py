# Generated by Django 4.1 on 2022-08-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_account_discord_account_github_account_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер моб. телефона'),
        ),
    ]