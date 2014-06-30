# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response

__author__ = 'ajaxj'

def home(request):
    return render_to_response("index.html")