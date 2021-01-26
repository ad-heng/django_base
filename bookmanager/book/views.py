from django.shortcuts import render

# Create your views here.

"""
视图函数2个要求：
1.视图函数第一个参数是接收请求，即HttpRequest的类对象
2.必须返回一个响应

"""

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    context={
        'name':'马上双十一，戳我有惊喜'
    }
    return render(request,'book/index.html',context=context)
