# -*- coding:utf-8 -*-

# 引入flask 扩展
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
__all__=['db','cache']
cache = Cache()
db = SQLAlchemy()