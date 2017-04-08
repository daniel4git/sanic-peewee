# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   05-Apr-2017
@Email:  hsz1273327@gmail.com
# @Last modified by:   Huang Sizhe
# @Last modified time: 08-Apr-2017
@License: MIT
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
    """针对表格操作的Mixin.同步阻塞操作
    """

    def create_tables(self, model_classes, log=log, safe=False):
        """创建表格,modle中定义的约束也会一并被创建

        Parameters:
            model_classes (list): - model列表,注意类型不是string
            log (logging): - python标准库的logging对象,默认使用sanic.log.log
            safe (bool): - 默认False,如果为True,已经存在的表格将不会被创建
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
        """删除表格

        Parameters:
            model_classes (list<class>): - model列表,注意类型不是string
            log (logging): - python标准库的logging对象,默认使用sanic.log.log
            safe (bool): - 默认False,如果为True,则会先校验表格是否存在,然后再进行删除
            cascade (bool): - 默认False,选择是否使用串联删除,串联删除是指在表下有对象的情况下连对象一并删除.
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
    """异步事务处理"""

    def async_atomic(self):
        """原子操作

        Example:
        obj = await TestModel.aio.create(text='FOO')
        obj_id = obj.id
        async with db.async_atomic():
            obj.text = 'BAR'
            await objects.update(obj)
        """
        return atomic(self.db)

    def async_savepoint(self):
        """savepoint操作,也和async_atomic一样用async with"""
        return savepoint(self.db)

    def async_transaction(self):
        """事务操作,也和async_atomic一样用async with """
        return transaction(self.db)

class QueryHandlerMixin:
    """异步请求"""

    class aio:
        @staticmethod
        def execute(query):
            return execute(query)

        @staticmethod
        def insert(query, **data):
            """query需要是InsertQuery类型或者orm的model类"""
            if isinstance(query, InsertQuery):
                return insert(query)
            else:
                return create_object(query, **data)

        @staticmethod
        def select(query):
            """query需要是SelectQuery类型"""
            return select(query)

        @staticmethod
        def get(query, *args):
            """query需要是Query类型或者orm对象"""
            return get_object(query, *args)

        @staticmethod
        def update(query, only=None):
            """query需要是UpdateQuery类型或者orm对象"""
            if isinstance(query, UpdateQuery):
                return update(query)
            else:
                return update_object(query, only=only)

        @staticmethod
        def delete(query, recursive=False, delete_nullable=False):
            """query需要是DeleteQuery类型或者orm对象"""
            if isinstance(query, DeleteQuery):
                return delete(query)
            else:
                return delete_object(query,
                                     recursive=recursive,
                                     delete_nullable=delete_nullable)

        @staticmethod
        def prefetch(query, *subqueries):
            """预处理"""
            return prefetch(query, *subqueries)

        @staticmethod
        def scalar(query, as_tuple=False):
            """Scalar 函数"""
            return scalar(query, as_tuple=as_tuple)

        @staticmethod
        def count(query, clear_limit=False):
            """数个数"""
            return count(query, clear_limit=clear_limit)
