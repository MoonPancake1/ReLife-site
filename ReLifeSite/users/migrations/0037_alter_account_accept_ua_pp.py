# Generated by Django 4.1 on 2022-08-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_alter_account_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accept_ua_pp',
            field=models.BooleanField(blank=True, null=True, verbose_name='Согласие со всеми правилами'),
        ),
    ]
