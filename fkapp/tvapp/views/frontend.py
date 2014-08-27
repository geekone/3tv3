# -*- coding:utf-8 -*-

from flask import Module,render_template

frontend  = Module(__name__)

@frontend.route("/")
def index():
	return render_template("home/index.html")
