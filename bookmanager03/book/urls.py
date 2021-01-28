# -*- coding: utf-8 -*-#
# @Author : heng
# @File : urls.py
# @Software : PyCharm
# @Date : 2021/1/28
from django.urls import path

from book.views import create_book

urlpatterns=[
    path('create/',create_book)
]
