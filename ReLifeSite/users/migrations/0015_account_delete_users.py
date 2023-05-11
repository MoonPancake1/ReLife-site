# Generated by Django 4.1 on 2022-08-27 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(null=True, verbose_name='День рождения')),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], max_length=7)),
                ('img', models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='Аватарка')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь_доп',
                'verbose_name_plural': 'Пользователи_доп',
            },
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
