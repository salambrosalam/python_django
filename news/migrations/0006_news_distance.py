# Generated by Django 3.2.6 on 2022-09-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20220908_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='distance',
            field=models.TextField(blank=True, verbose_name='distance'),
        ),
    ]