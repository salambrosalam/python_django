# Generated by Django 3.2.6 on 2022-09-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='price',
            field=models.TextField(blank=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='news',
            name='telefon',
            field=models.TextField(blank=True, verbose_name='telefon'),
        ),
    ]
