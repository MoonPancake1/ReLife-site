# Generated by Django 4.1 on 2022-09-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_nov_views_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='nov',
            name='views_news',
        ),
        migrations.AddField(
            model_name='nov',
            name='views',
            field=models.ManyToManyField(blank=True, default=0, related_name='post_views', to='users.ip'),
        ),
    ]
