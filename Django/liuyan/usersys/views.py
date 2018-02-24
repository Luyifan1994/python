# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import RegistForm


# Create your views here.

def register(request):
    # ('next', '')中的''表示默认值为''
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    if request.method == 'POST':
        form = RegistForm(request.POST)

        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                return render(request, 'message/message.html')
    else:
        form = RegistForm()

    return render(request, 'registration/users/register.html', context={'form': form, 'next': redirect_to})


def index(request):
    return render(request, 'index.html')

