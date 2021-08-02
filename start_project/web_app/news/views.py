from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print(request)
    return HttpResponse('Hello World')

def test(request):
    print("salam")
    return HttpResponse("<H1>TEST PAGE</H1>")
