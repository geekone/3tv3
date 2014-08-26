#-*- coding:utf-8 -*-
import datetime
from django.db import models

#分类
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)

    class Meta:
        db_table = "t_categories"

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    class Meta:
        db_table = "t_tags"

    def __unicode__(self):
        return self.name

#视频
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("标题",max_length=100)
    category = models.ForeignKey(Category,related_name='category_movie')
    pubtime = models.DateField("发布时间",auto_now_add=True)
    tags = models.ManyToManyField(Tag)      #多对多
    class Meta:
        db_table = "t_movies"

    def __unicode__(self):
        return self.title

#文章
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,related_name="category_article")  #一对多
    pubtime = models.DateField("发布时间",auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    class Meta:
        db_table = "t_articles"

    def __unicode__(self):
        return self.title




#一对多test
# category = Category.objects.fiter(条件)
# articles = category.book_set.all()    #取出多
# category = article.category           #取出分类

#多对多 一个文章和视频有多个作者
class Author(models.Model):
    authorname = models.CharField(max_length=30)

    class Meta:
        db_table = "t_authors"

    def __unicode__(self):
        return self.authorname


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
        