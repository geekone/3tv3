from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from backend.models import Category,Movie,Car,Engine


def index(request):
    return render_to_response("backend/index.html")


# category all list
def categories(request):
    category = Category()
    category.name = "name1"
    category.cname = "nam3"
    category.save()
    _categories = Category.objects.all()
    return render_to_response("backend/categories.html")


# movie all list
def movies(request):
	_movies = Movie.objects.all()
	return render_to_response("backend/movies.html")




# init database 
def initdb(request):
	e = Engine()
	e.name = "car1eng1"
	e.save()
	c = Car()
	c.name = "car1"
	c.engine = e 
	c.save()
	return HttpResponseRedirect("/backend/")  



	# category = Category()
	# category.name = "name1"
	# category.cname = "cname1"
	# category.save()
	# movie = Movie()
	# movie.title = "title1"
	# movie.save()
	# return ""
