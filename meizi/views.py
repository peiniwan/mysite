# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pymysql
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from meizi.models import Meizis, StandardResultSetPagination
from meizi.serializers import MeiziSerializer, ListSerialize, ListPicSerialize


@api_view(['GET'])
def getlist(request, format=None):
    if request.method == 'GET':
        meizis = Meizis.objects.all()
        serializer = MeiziSerializer(meizis, many=True)
        # return Response(serializer.data)

        # http: // 127.0.0.1:8000 / getlist?limit = 20
        # http: // 127.0.0.1:8000 / getlist?limit = 20 & offset = 20
        # http: // 127.0.0.1:8000 / getlist?limit = 20 & offset = 40
        # 根据url参数 获取分页数据
        obj = StandardResultSetPagination()
        page_list = obj.paginate_queryset(meizis, request)
        # 对数据序列化 普通序列化 显示的只是数据
        ser = ListSerialize(instance=page_list, many=True)  # 多个many=True # instance：把对象序列化
        response = obj.get_paginated_response(ser.data)
        return response


@api_view(['GET', 'POST'])
def getlispic(request, format=None):
    if request.method == 'GET':
        mid = request.GET['mid']
        if mid is not None:
            # get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
            meizis = Meizis.objects.filter(mid=mid)
            obj = StandardResultSetPagination()
            page_list = obj.paginate_queryset(meizis, request)
            ser = ListPicSerialize(instance=page_list, many=True)
            response = obj.get_paginated_response(ser.data)
            return response
        else:
            return Response(str('请传mid'))
