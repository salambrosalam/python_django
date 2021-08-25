from django.shortcuts import render
from django.http import HttpResponse

from .models import News

# Create your views here.

def index(request):
    print(request)
    news = News.objects.all()
    return render(request, "news/index.html", {"news": news, "title": "Список новостей"})

def test(request):
    print("salam")
    return HttpResponse("<H1>TEST PAGE</H1> ")
