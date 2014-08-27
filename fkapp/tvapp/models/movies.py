# -*- coding:utf-8 -*-

from tvapp.extensions import db

class Movie(db.Model):
	__tablename__ = 'movies'

	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(100))

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title