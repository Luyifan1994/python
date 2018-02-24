# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Message(models.Model):
    messuser = models.CharField(max_length=30)
    content = models.TextField(max_length=256)
    pubtime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.messuser
