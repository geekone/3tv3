#-*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from backend.models import Category,Movie,Article,Car,Engine
from django.template import RequestContext

def index(request):
    return render_to_response("backend/index.html")


# category all list
def categories(request):
    _categories = Category.objects.all()
    return render_to_response("backend/categories.html",{'categories':_categories})

#添加分类
def category_add(request):
	if request.method == "POST":
		_name = request.POST['name']
		_cname = request.POST['cname']
		category = Category()
		category.name = _name
		category.cname = _cname
		category.save()
		return HttpResponseRedirect("/backend/categories")
	else:
		return render_to_response("backend/category_add.html",None,context_instance=RequestContext(request))

def category_edit(request,category_id):
	if request.method == "POST":
		_id = request.POST['categoryid']
		_name = request.POST['name']
		_cname = request.POST['cname']
		category = Category.objects.get(pk=_id)
		category.name = _name
		category.cname = _cname
		category.save()
		return HttpResponseRedirect("/backend/categories")
	else:
		category = Category.objects.get(pk=category_id)
		data = {'category':category}
		return render_to_response("backend/category_edit.html",data,context_instance=RequestContext(request))

#删除分类通过ID
def category_del(request,category_id):
	category = Category.objects.get(pk=category_id)
	category.delete()
	return HttpResponseRedirect("/backend/categories")




# movie all list
def movies(request):
	_movies = Movie.objects.all()
	return render_to_response("backend/movies.html")




# init database 
def initdb(request):
	# e = Engine()
	# e.name = "car1eng1"
	# e.save()
	# c = Car()
	# c.name = "car1"
	# c.engine = e 
	# c.save()
	# c1 = Category()
	# c1.name = "c1"
	# c1.cname = "c1"
	# c1.save()
	# c2 = Category()
	# c2.name = "c2"
	# c2.cname = "c2"
	# c2.save()
	# c1 = Category.objects.filter(name='c2')  
	# print c1[0].name,c1[0].cname

	# c1 = Category.objects.get(pk=1)
	# c2 = Category.objects.get(pk=2)

	# a1 = Article()
	# a1.title = "a1"
	# a1.category = c1
	# a1.save()

	# a2 = Article()
	# a2.title = "a2"
	# a2.category = c1
	# a2.save()

	# a3 = Article()
	# a3.title = "a3"
	# a3.category = c2
	# a3.save()

	# 一对多查询
	# c1 = Category.objects.get(pk=1)	#通过related_name查找
	# artilces = c1.category_article.all()
	# print artilces

	# a_list = Article.objects.filter(category__name__contains='c1')	#另一种方式
	# print a_list

	# category = Category.objects.filter(category_article__title='a3')	#反向
	# print category # print category

	#一对多级联删除
	# c1 = Category.objects.get(pk=1)
	# c1.delete()
	Article.objects.get(pk=3).delete()

	return HttpResponseRedirect("/backend/")  



	# category = Category()
	# category.name = "name1"
	# category.cname = "cname1"
	# category.save()
	# movie = Movie()
	# movie.title = "title1"
	# movie.save()
	# return ""
