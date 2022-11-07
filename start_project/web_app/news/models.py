from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Name")
    content = models.TextField(blank=True, verbose_name="Content")
    distance = models.TextField(blank=True, verbose_name="distance")
    price = models.TextField(blank=True, verbose_name="price")
    telefon = models.TextField(blank=True, verbose_name="telefon")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updates")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Image", blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name="Category name")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Task"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Category name")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"
        ordering = ["title"]