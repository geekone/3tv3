#-*- coding:utf-8 -*-
import datetime
from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)

    class Meta:
        db_table = "t_categories"

    def __unicode__(self):
        return self.name


class Movie(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)

	class Meta:
		db_table = "t_movies"

	def __unicode__(self):
		return self.title


