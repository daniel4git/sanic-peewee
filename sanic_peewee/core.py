# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   huangsizhe
@Last modified time: 01-Apr-2017
@License: MIT
@Description:
"""


import peewee
from peewee import Model, BaseModel
from peewee_async import Manager, PostgresqlDatabase, MySQLDatabase, execute
from functools import partial


def database(dbtype, *args, **kwargs):
    TYPES = {
        "postgresql": PostgresqlDatabase,
        "pg": PostgresqlDatabase,
        "mysql": MySQLDatabase
    }

    def _raise():
        raise AttributeError("unknow db type")
    return TYPES.get(dbtype, lambda *as, **ks: _raise())(*args, **kwargs)


class Peewee:

    def _get_meta_db_class(self):
    """creating a declartive class model for db"""
        class _BlockedMeta(BaseModel):
            def __new__(cls, name, bases, attrs):
                _instance = super(_BlockedMeta, cls).__new__(cls, name, bases, attrs)
                _instance.async = AsyncManager(_instance, self.db)
                return _instance

        class AsyncBase(Model, metaclass=_BlockedMeta):

            def to_dict(self):
                return self._data

            class Meta:
                database=self.db

        return AsyncBase

    def __call__(self, app=None):
        if app:
            self.init_app(app)
        else:
            raise AttributeError("need a sanic app to init the extension")

    def __init__(self, db=None):
        self.db = db

    def init_app(self, app):
        if not self.db:
            if all(app.config.DB_TYPE,
                    app.config.DB_HOST,
                    app.config.DB_USER,
                    app.config.DB_PASSWORD,
                    app.config.DB_NAME):
                if app.config.DB_PORT:
                    self.db = database(dbtype=app.config.DB_TYPE,
                             database=app.config.DB_NAME,
                             host=app.config.DB_HOST,
                             port=app.config.DB_PORT,
                             user=app.config.DB_USER,
                             password=app.config.DB_PASSWORD)
                else:
                    self.db = database(dbtype=app.config.DB_TYPE,
                             database=app.config.DB_NAME,
                             host=app.config.DB_HOST,
                             user=app.config.DB_USER,
                             password=app.config.DB_PASSWORD)

        self.manager = peewee_async.Manager(self.db)
        self.AsyncModel = self._get_meta_db_class()
        app.extensions['SanicPeewee'] = self
        return self

    def create_tables(self,model_class,safe=False):
        return self.db.create_tables(model_class,safe)

    def drop_tables(self,models, safe=False, cascade=False):
        return self.db.drop_tables(self,models, safe, cascade)
