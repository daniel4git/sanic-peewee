# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 05-Apr-2017
@License: MIT
@Description:
"""
__all__=["Core"]

import peewee
from peewee import Model, BaseModel
from peewee_async import Manager, execute
from peewee_async import PostgresqlDatabase, MySQLDatabase,  PooledMySQLDatabase, PooledPostgresqlDatabase
from peewee_asyncext import PostgresqlExtDatabase, PooledPostgresqlExtDatabase
from functools import partial

from async_manager import AsyncManager
from playhouse.db_url import parse

class Core:

    def _database(self,DBURL=None):
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
            if DBURL.find("://")<0:
                raise AttributeError("you need to input a database url")
            else:
                dbtype = DBURL.split("://")[0]
                return TYPES.get(dbtype, lambda *as, **ks: _raise())(**parse(DBURL))


    def __call__(self, app=None):
        if app:
            self.init_app(app)
        else:
            raise AttributeError("need a sanic app to init the extension")

    def __init__(self,DBURL=None):
        """根据参数选择生成db,参数为dburl的形式

        """
        if DBURL:
            self.db = self._database(DBURL)

    def init_app(self, app):
        if not self.db:
            if app.config.DBURL:
                self.db = self._database(app.config.DBURL)

        self.AsyncModel = self._get_meta_db_class()
        app.extensions['SanicPeewee'] = self
        return self
    def _get_meta_db_class(self):
    """creating a declartive class model for db"""
        db = self.db
        class _BlockedMeta(BaseModel):
            def __new__(cls, name, bases, attrs):
                _instance = super(_BlockedMeta, cls).__new__(cls, name, bases, attrs)
                _instance.async = AsyncManager(_instance,db)
                return _instance

        class AsyncBase(Model, metaclass=_BlockedMeta):
            # @classmethod
            # def createTable(clz):
            #     database = clz.Meta.database
            #     database.set_allow_sync(True)
            #     try:
            #         clz.create_table(True)
            #         database.close()
            #     except:
            #         print("table Exist")
            #     database.set_allow_sync(False)
            def to_dict(self):
                return self._data

            class Meta:
                database=db

        return AsyncBase
