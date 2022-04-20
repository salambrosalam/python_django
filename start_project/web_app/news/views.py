from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category

# Create your views here.

def index(request):
    print(request)
    news = News.objects.all()
    categories = Category.objects.all()

    context = {
        "news": news,
        "title": "Список новостей",
        "categories": categories
    }

    return render(request, "news/index.html", context=context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    context = {
        "news": news,
        "categories": categories,
        "category": category
    }

    return render(request, "news/category.html", context=context)