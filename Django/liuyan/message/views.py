# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from models import Message
from forms import MessForm
# from usersys.models import User


# Create your views here.
def messinfo(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MessForm(request.POST)
            if request.POST.has_key("delete"):
                Message.objects.all().delete()
            if form.is_valid():
                name = form.cleaned_data['name']
                content = form.cleaned_data['content']
                Message.objects.create(messuser=name, content=content)
                # messlist = Message.objects.all()
                return HttpResponseRedirect(reverse('message'))
        else:
            return redirect('index')
    else:
        form = MessForm()
    messdb = Message.objects.order_by('-pubtime')

    return render(request, 'message/message.html', context={'form': form, 'messdb': messdb})
