from __future__ import absolute_import, unicode_literals

from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=80)
