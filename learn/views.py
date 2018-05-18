# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(u"欢迎光临")


def home(request):
    # return render(request, 'home.html')
    string = u"我在学习Django，用它来建网站"
    # html里这样用{{string}}
    return render(request, 'home.html', {'string': string})
