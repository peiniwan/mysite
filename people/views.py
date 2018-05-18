# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from people.models import Person


def create(request):
    # 新建一个对象的方法有以下几种：
    Person.objects.create(name='liu', age=18)
    # p = Person(name="WZ", age=23)
    # p = Person(name="TWZ")
    # p.age = 23
    # p.save()
    # 这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，第一个为Person对象，
    # 第二个为True或False, 新建时返回的是True, 已经存在时返回False
    # Person.objects.get_or_create(name="WZT", age=23)
    s = Person.objects.get(name='liu')
    return HttpResponse(str(s))
