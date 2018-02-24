#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/18 下午1:58
# @Author  : Ivan
# @File    : forms.py
# @Function: 表单操作

from django.contrib.auth.forms import UserCreationForm
from models import User

# 使用Django自带的UserCreationForm作为用户注册表单，并用自定义的User模型
class RegistForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User  #
        fields = ('username', 'email')  #代表注册时需要填写哪些信息
