#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/19 下午7:52
# @Author  : Ivan
# @File    : forms.py
# @Function:

from django import forms


class MessForm(forms.Form):
    name = forms.CharField(label=u'姓名', max_length=30)
    content = forms.CharField(label=u'内容', widget=forms.TextInput(
        {'style': 'width:200px;height:50px'}))  # 使用widget可以conent对应的标签中添加属性
