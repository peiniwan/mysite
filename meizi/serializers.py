# -*- coding: utf-8 -*-
from rest_framework import serializers

from meizi.models import Meizis
from snippets.models import Snippet


class MeiziSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = Meizis
        # 和"__all__"等价
        fields = ('mid', 'title', 'picname', 'page_url', 'img_url')


# 自带的分页功能
class ListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Meizis
        # fields = "__all__"
        fields = ('mid', 'title')


class ListPicSerialize(serializers.ModelSerializer):
    class Meta:
        model = Meizis
        fields = "__all__"
