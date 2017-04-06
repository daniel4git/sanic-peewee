# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 06-Apr-2017
@License: MIT
@Description:
"""
__all__ = ["Core"]

import peewee
from peewee import Model, BaseModel
from peewee_async import Manager, execute
from peewee_async import PostgresqlDatabase, MySQLDatabase,  PooledMySQLDatabase, PooledPostgresqlDatabase
from peewee_asyncext import PostgresqlExtDatabase, PooledPostgresqlExtDatabase
from functools import partial

from sanic_peewee.async_manager import AsyncManager
from playhouse.db_url import parse


class Core:
    """核心类,作为Peewee的父类,主要是管数据库连接,与sainc对象绑定,以及生成model父类
    """

    def _database(self, DBURL=None):
        """
        _database用于创建数据库的async连接

        Parameters:
        DBURL (str): - batabase url

        Return:
            object: - 不同数据库连接的对象



        dburl例子如下:
        postgresql://user:password@ip:port/dbname
        mysql://user:passwd@ip:port/dbname
        mysql+pool://user:passwd@ip:port/dbname?max_connections=20&stale_timeout=300
        postgresql+pool://user:passwd@ip:port/dbname?max_connections=20&stale_timeout=300
        postgresqlext://user:passwd@ip:port/dbname
        postgresqlext+pool://user:passwd@ip:port/dbname?max_connections=20&stale_timeout=300
        """
        TYPES = {
            "postgresql": PostgresqlDatabase,
            "mysql": MySQLDatabase,
            "postgresql+pool": PooledPostgresqlDatabase,
            "mysql+pool": PooledMySQLDatabase,
            "postgresqlext": PostgresqlDatabase,
            "postgresqlext+pool": PooledPostgresqlExtDatabase,
        }

        def _raise():
            raise AttributeError("unknow db type")
        if DBURL:
            if DBURL.find("://") < 0:
                raise AttributeError("you need to input a database url")
            else:
                dbtype = DBURL.split("://")[0]
                dbinfo = parse(DBURL)
                dbinfo["password"] = dbinfo["passwd"]
                del dbinfo["passwd"]
                return TYPES.get(dbtype, lambda **ks: _raise())(**dbinfo)

    def __call__(self, app=None):
        if app:
            return self.init_app(app)
        else:
            raise AttributeError("need a sanic app to init the extension")

    def __init__(self, DBURL=None):
        """根据参数选择生成db,参数为dburl的形式

        """
        if DBURL:
            self.db = self._database(DBURL)

    def init_app(self, app):
        """绑定app
        """
        if not self.db:
            if app.config.DBURL:
                self.db = self._database(app.config.DBURL)

        self.AsyncModel = self._get_meta_db_class()
        print(self.AsyncModel)
        if "extensions" not in app.__dir__():
            app.extensions = {}
        app.extensions['SanicPeewee'] = self
        return self

    def _get_meta_db_class(self):
        """creating a declartive class model for db"""
        db = self.db

        class _BlockedMeta(BaseModel):
            def __new__(cls, name, bases, attrs):
                _instance = super(_BlockedMeta, cls).__new__(
                    cls, name, bases, attrs)
                _instance.aio = AsyncManager(_instance, db)
                return _instance

        class AsyncBase(Model, metaclass=_BlockedMeta):
            def to_dict(self):
                return self._data

            class Meta:
                database = db

        return AsyncBase
