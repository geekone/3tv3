#-*- coding:utf-8 -*-
import datetime
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)

    class Meta:
        db_table = "t_category"

    def __unicode__(self):
        return self.name

