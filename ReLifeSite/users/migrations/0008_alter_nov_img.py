# Generated by Django 4.1 on 2022-08-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_nov_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nov',
            name='img',
            field=models.ImageField(null=True, upload_to='news/', verbose_name='Превью'),
        ),
    ]