# -*- coding:utf-8 -*-

from tvapp.extensions import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(50))

	def __str__(self):
		return self.username

	def __repr__(self):
		return self.username