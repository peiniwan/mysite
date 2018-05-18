# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 引入我们创建的表单类
from .forms import AddForm

# 比如用户输入的不是数字，而是字母，就出错了，还有就是提交后再回来已经输入的数据也会没了。
# 当然如果我们手动将输入之后的数据在 views 中都获取到再传递到网页，这样是可行的，但是很不方便，
# 所以 Django 提供了更简单易用的 forms 来解决验证等这一系列的问题。
def index(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
