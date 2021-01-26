# -*- coding: utf-8 -*-#
# @Author : heng
# @File : urls.py
# @Software : PyCharm
# @Date : 2021/1/26
from django.urls import path

from book.views import index

urlpatterns=[
    path('index/',index)
]
