# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import processes
from .models import instances
from .models import task

# Register your models here.

admin.site.register(processes)
admin.site.register(instances)
admin.site.register(task)

