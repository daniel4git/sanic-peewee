# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
# @Last modified by:   Huang Sizhe
# @Last modified time: 08-Apr-2017
@License: Apache License Version 2.0
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
    """
    """

    def _database(self, DBURL=None):
        """
        _database is used to create a async connection with db.

        Parameters:
        DBURL (str): - batabase url

        Return:
            object: - db connection object



        dburl's example:
            postgresql://user:password@ip:port/dbname
            mysql://user:passwd@ip:port/dbname
            mysql+pool://user:passwd@ip:port/dbname?max_connections=20
            postgresql+pool://user:passwd@ip:port/dbname?max_connections=20
            postgresqlext://user:passwd@ip:port/dbname
            postgresqlext+pool://user:passwd@ip:port/dbname?max_connections=20
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
                if dbinfo.get("passwd"):
                    dbinfo["password"] = dbinfo["passwd"]
                    del dbinfo["passwd"]
                return TYPES.get(dbtype, lambda **ks: _raise())(**dbinfo)

    def __call__(self, app=None):
        if app:
            return self.init_app(app)
        else:
            raise AttributeError("need a sanic app to init the extension")

    def __init__(self, DBURL=None):
        if DBURL:
            self.db = self._database(DBURL)
        else:
            self.db = None

    def init_app(self, app):
        """bind the app
        """
        if not self.db:
            if app.config.DB_URL:
                self.db = self._database(app.config.DB_URL)
            else:
                raise AssertionError("need a db url")

        self.AsyncModel = self._get_meta_db_class()
        if "extensions" not in app.__dir__():
            app.extensions = {}
        app.extensions['SanicPeewee'] = self
        return self

    def close(self):
        return self.db.close_async()

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
