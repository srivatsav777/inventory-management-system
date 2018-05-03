# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class processes(models.Model):
   process_name=models.CharField(max_length=10)
   process_state=models.CharField(max_length=10)
   process_id=models.IntegerField()


   def __str__(self):
      return self.process_name



class instances(models.Model):
   instance_name=models.CharField(max_length=10)
   instance_state=models.CharField(max_length=10)
   instance_id=models.IntegerField()


   def __str__(self):
      return self.instance_name


class task(models.Model):
   task_name=models.CharField(max_length=10)
   task_state=models.CharField(max_length=10)
   task_id=models.IntegerField()


   def __str__(self):
      return self.task_name



