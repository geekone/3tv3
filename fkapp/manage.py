# -*- coding:utf-8 -*- 
from flask import Flask, current_app
from flask.ext.script import Server,Shell,Manager,Command,prompt_bool

from tvapp import create_app	#导入 tvapp 
from tvapp.extensions import db

from tvapp.models.users import User

manager = Manager(create_app("config.cfg"))		#初始化一个应用程序 create_app返回 app 对象
manager.add_command("runserver",Server('0.0.0.0',port=8080))	#给manager对象添加runserver命令

#给shell添加db对象
def _make_context():
	return dict(db=db)

manager.add_command("shell",Shell(make_context=_make_context))


@manager.command
def createall():
	"create database"
	db.create_all()

@manager.command
def dropall():
	"drops all database"
	db.drop_all()

if __name__ == '__main__':
	manager.run()