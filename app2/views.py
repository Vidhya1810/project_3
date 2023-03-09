from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Nani(request):
    return HttpResponse('<marquee><h1>Nani is a goodboy<h1/><marquee/>')

def Vijji(return):
    return HttpResponse('<marquee><h1>Vijji is a good girl<h1/><marquee/>')
