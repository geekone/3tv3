from django.shortcuts import render, render_to_response

# Create your views here.
from backend.models import Category


def index(request):
    _categories = Category.objects.all()
    print _categories
    return render_to_response("app/index.html",{'categories':_categories})