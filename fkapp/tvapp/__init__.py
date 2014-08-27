# -*- coding:utf-8 -*-


from flask import Flask
from tvapp import views
from tvapp.extensions import db,cache

DEFAULT_APP_NAME = "tvapp"

#多模块配置
DEFAULT_MODULES = (
	(views.frontend,""),
	(views.backend,"/backend"),
)

#初始项目  读取配置文件
def create_app(config=None,modules=None):
	if modules is None:
		modules = DEFAULT_MODULES
		
	app = Flask(DEFAULT_APP_NAME)
	app.config.from_pyfile(config)
	
	configure_extensions(app)		#装载扩展
	configure_modules(app,modules)	#装载模块

	return app 


def configure_extensions(app):
	db.init_app(app)
	# cache.init_app(app)

def configure_modules(app,modules):
	for module,url_prefix in modules:
		app.register_module(module,url_prefix=url_prefix)