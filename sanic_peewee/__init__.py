"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@License: MIT
"""
__all__ = ["select", "prefetch", "scalar", "atomic", "savepoint", "transaction", "count",
           "create", "delete", "get", "insert", "update", "Peewee"]

# 搜索
from peewee_async import select
# 数据预取
from peewee_async import prefetch
# 相当于select(),但数据为一个整体
from peewee_async import scalar
"""事务操作,配合`async with`使用
"""
from peewee_async import atomic  # 原子操作
from peewee_async import savepoint  # 保存点
from peewee_async import transaction  # 事务

# 结果计数,相当于`.count()`
from peewee_async import count
"""增删改查"""
from peewee_async import create_object as create
from peewee_async import delete_object as delete
from peewee_async import get_object as get
from peewee_async import insert
from peewee_async import update_object as update

from sanic_peewee.core import Core
from sanic_peewee.mixins import TableHandlerMixin, TransactionHandlerMixin, QueryHandlerMixin

from peewee import SelectQuery, UpdateQuery, InsertQuery, DeleteQuery


class Peewee(Core, TableHandlerMixin, TransactionHandlerMixin, QueryHandlerMixin):
    """
    Attributes:
        db (db): - 数据库原始的连接
        AsyncModel (class): - 用于创建model的父类
        aio (class): - 用于封装数据操作的命名空间
        SelectQuery (peewee.SelectQuery) : - 用户select的请求
        UpdateQuery (peewee.UpdateQuery) : - 用于update的请求
        InsertQuery (peewee.InsertQuery) : - 用于插入数据的请求
        DeleteQuery (peewee.DeleteQuery) : - 用于删除数据的请求
    """

    SelectQuery = SelectQuery
    UpdateQuery = UpdateQuery
    InsertQuery = InsertQuery
    DeleteQuery = DeleteQuery

    def __init__(self, db=None):
        super().__init__(db)
