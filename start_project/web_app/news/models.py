from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Картинка", blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Название категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Название категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]