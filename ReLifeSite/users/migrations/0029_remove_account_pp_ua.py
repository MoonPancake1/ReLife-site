# Generated by Django 4.1 on 2022-08-29 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_account_pp_ua'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='pp_ua',
        ),
    ]
