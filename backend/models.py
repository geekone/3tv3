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


# OneToOneField    has one: one to one

# ManyToManyField  has many : lots of A belong to B and B has many A

class Engine(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=25)
    engine = models.OneToOneField(Engine,unique=True)

    def __unicode__(self):
        return self.name

# ForeignKey  belong to: ForeignKey all in one
class Engine2(models.Model):
    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

class Car2(models.Model):
    name = models.CharField(max_length=25)
    engine = models.ForeignKey(Engine2)

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    firstname = models.CharField(max_length=30)

    def __unicode__(self):
        return self.firstname

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)

    def __unicode__(self):
        return self.title
        