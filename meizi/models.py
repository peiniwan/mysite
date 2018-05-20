# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pymysql
from django.db import models

# Create your models here.
from rest_framework.pagination import LimitOffsetPagination


class Meizis(models.Model):
    mid = models.CharField(max_length=10)
    title = models.CharField(max_length=50, blank=True, null=True)
    picname = models.CharField(max_length=10, blank=True, null=True)
    page_url = models.CharField(max_length=50, blank=True, null=True)
    img_url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meizi_meizis'


class StandardResultSetPagination(LimitOffsetPagination):
    # 默认每页显示的条数
    default_limit = 20
    # url 中传入的显示数据条数的参数
    limit_query_param = 'limit'
    # url中传入的数据位置的参数
    offset_query_param = 'offset'
    # 最大每页显示条数
    max_limit = None
