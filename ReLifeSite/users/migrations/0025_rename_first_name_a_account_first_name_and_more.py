# Generated by Django 4.1 on 2022-08-28 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_alter_account_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='first_name_a',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='last_name_a',
            new_name='last_name',
        ),
    ]
