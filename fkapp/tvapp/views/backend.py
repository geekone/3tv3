# -*- coding:utf-8 -*-

from flask import Module,render_template

backend = Module(__name__)

@backend.route("/")
def index():
	return render_template("admin/index.html")