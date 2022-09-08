# Generated by Django 3.2.6 on 2022-09-08 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Task', 'verbose_name_plural': 'Task'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updates'),
        ),
    ]
