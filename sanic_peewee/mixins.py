# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   05-Apr-2017
@Email:  hsz1273327@gmail.com
# @Last modified by:   Huang Sizhe
# @Last modified time: 08-Apr-2017
@License: Apache License Version 2.0
"""
__all__ = ["TableHandlerMixin", "TransactionHandlerMixin", "QueryHandlerMixin"]
from sanic.log import log
from peewee_async import atomic
from peewee_async import savepoint
from peewee_async import transaction

from peewee_async import prefetch
from peewee_async import scalar
from peewee_async import count
from peewee_async import execute

from peewee_async import create_object, insert
from peewee_async import delete_object, delete
from peewee_async import get_object, select
from peewee_async import update_object, update

from peewee import InternalError

from peewee import SelectQuery, UpdateQuery, InsertQuery, DeleteQuery


class TableHandlerMixin:
    """

    Mixing for table operations. Synchronous blocking operation
    """

    def create_tables(self, model_classes, log=log, safe=False):
        """create tables,The constraints defined in model will also be created

        Parameters:
            model_classes (list): - model's list ,the type is not string
            log (logging): - logging object,default sanic.log.log
            safe (bool): - default False,if True,the exist table will not be created
        """
        database = self.db
        database.set_allow_sync(True)
        try:
            database.create_tables(model_classes, safe)
            log.info("created_table")
            database.close()
        except InternalError as exist:
            log.info("table exist")
            return False
        except Exception as e:
            raise e
        else:
            return True
        finally:
            database.set_allow_sync(False)

    def drop_tables(self, model_classes, log=log, safe=False, cascade=False):
        """delete tables

        Parameters:
            model_classes (list<class>): - model's list ,the type is not string
            log (logging): - logging object,default sanic.log.log
            safe (bool): - default False,if True,peewee will check if the table is exist first
            cascade (bool): - default False,if True ,peewee will delete the cascade table also.
        """
        database = self.db
        database.set_allow_sync(True)
        try:
            database.drop_tables(model_classes, safe, cascade)
            log.info("droped_table")
            database.close()
        except InternalError as exist:
            log.info("interinterErrornalError")
            return False
        except Exception as e:
            raise e
        else:
            return True
        finally:
            database.set_allow_sync(False)


class TransactionHandlerMixin:

    def async_atomic(self):
        """atomic

        Example:
        obj = await TestModel.aio.create(text='FOO')
        obj_id = obj.id
        async with db.async_atomic():
            obj.text = 'BAR'
            await objects.update(obj)
        """
        return atomic(self.db)

    def async_savepoint(self):

        return savepoint(self.db)

    def async_transaction(self):

        return transaction(self.db)


class QueryHandlerMixin:

    class aio:

        @staticmethod
        def execute(query):
            return execute(query)

        @staticmethod
        def insert(query, **data):

            if isinstance(query, InsertQuery):
                return insert(query)
            else:
                return create_object(query, **data)

        @staticmethod
        def select(query):

            return select(query)

        @staticmethod
        def get(query, *args):

            return get_object(query, *args)

        @staticmethod
        def update(query, only=None):

            if isinstance(query, UpdateQuery):
                return update(query)
            else:
                return update_object(query, only=only)

        @staticmethod
        def delete(query, recursive=False, delete_nullable=False):

            if isinstance(query, DeleteQuery):
                return delete(query)
            else:
                return delete_object(query,
                                     recursive=recursive,
                                     delete_nullable=delete_nullable)

        @staticmethod
        def prefetch(query, *subqueries):
            return prefetch(query, *subqueries)

        @staticmethod
        def scalar(query, as_tuple=False):

            return scalar(query, as_tuple=as_tuple)

        @staticmethod
        def count(query, clear_limit=False):
            return count(query, clear_limit=clear_limit)
