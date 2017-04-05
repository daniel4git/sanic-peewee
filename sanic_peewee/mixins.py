# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   05-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 05-Apr-2017
@License: MIT
@Description:
"""
__all__=["TableHandlerMixin"]
from sanic.log import log
from peewee_async import async_atomic
from peewee_async import async_savepoint
from peewee_async import async_transaction
class TableHandlerMixin:
    """针对表格操作的Mixin.
    """
    def create_tables(self,model_classes,log=log,safe=False):
        """创建表格,modle中定义的约束也会一并被创建
        Parameters:
            model_classes (list<class>): - model列表,注意类型不是string
            log (logging): - python标准库的logging对象,默认使用sanic.log.log
            safe (bool): - 默认False,如果为True,已经存在的表格将不会被创建
        """
        database = self.db
        database.set_allow_sync(True)
        try:
            database.create_tables(model_classes,safe)
            log.info("created_table")
            database.close()
        except peewee.InternalError as exist:
            log.info("table exist")
        except Exception as e:
            raise e
        finally:
            database.set_allow_sync(False)

    def drop_tables(self,model_classes, log=log,safe=False,cascade=False):
        """删除表格,
        Parameters:
            model_classes (list<class>): - model列表,注意类型不是string
            log (logging): - python标准库的logging对象,默认使用sanic.log.log
            safe (bool): - 默认False,如果为True,则会先校验表格是否存在,然后再进行删除
            cascade (bool): - 默认False,选择是否使用串联删除,串联删除是指在表下有对象的情况下连对象一并删除.
        """
        database = self.db
        database.set_allow_sync(True)
        try:
            database.drop_tables(model_classes,safe,cascade)
            log.info("droped_table")
            database.close()
        except peewee.InternalError as exist:
            log.info("interinterErrornalError")
        except Exception as e:
            raise e
        finally:
            database.set_allow_sync(False)


class TransactionhandlerMixin:
    """事务处理
    """
    def atomic(self):
        return async_atomic(self.db)
    def savepoint(self):
        return async_savepoint(self.db)
    def transaction(self):
        return async_transaction(self.db)
