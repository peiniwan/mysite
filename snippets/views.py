# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.shortcuts import render
import pdb;


# Create your views here.
# @csrf_exempt
# def snippet_list(request):
#     """
#     request.POST  # 只能处理表单(form)数据，只能处理“POST”方法.
#     request.data  # 处理任意数据.可以处理'POST', 'PUT' 和 'PATCH'方法.
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         # 可以将queryset序列化。只需在序列器的参数中加入many = True
#         # 该代码是把刚刚保存的数据snippet对象，经过序列化保存成一个字典
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():  # 验证数据是否符合要求
#             serializer.save()
#             # serializer.data 数据创建成功后所有数据
#             return JsonResponse(serializer.data, status=201)
#         # serializer.errors 错误信息
#         return JsonResponse(serializer.errors, status=400)


# REST框架提供了两种编写API视图的封装。
# 1.@api_view装饰器，基于方法的视图。
# 2.继承APIView类，基于类的视图。
# request.data会自行处理输入的json请求
# 我们不再需要在views.py文件中使用JSONResponse类，所以可以删除它。然后，我们可以稍微重构我们的代码
# 使用格式后缀明确的指向指定的格式，需要添加一个format关键字参数
# http http://127.0.0.1:8000/snippets.json  # JSON 后缀
# http://127.0.0.1:8000/snippets.api   # 可视化 API 后缀
# http://127.0.0.1:8000/snippets/ code="print 123"post

@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# 重构
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    snippet的读取, 更新 或 删除
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # @register.filter
    # def pdb(element):
    #     pdb.set_trace()
    #     return element
    #
