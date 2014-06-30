from django.shortcuts import render, render_to_response
from backend.models import Category


def index(request):
    return render_to_response("backend/index.html")



def categories(request):
    category = Category()
    category.name = "name1"
    category.cname = "nam3"
    category.save()
    _categories = Category.objects.all()
    return render_to_response("backend/categories.html")
