"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@License: Apache License Version 2.0
"""
__all__ = ["select", "prefetch", "scalar", "atomic", "savepoint", "transaction",
"count","create", "delete", "get", "insert", "update", "Peewee"]


from peewee_async import select
from peewee_async import prefetch
from peewee_async import scalar

#transaction operation,work with `async with`
from peewee_async import atomic
from peewee_async import savepoint
from peewee_async import transaction

from peewee_async import count

#CRUD
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

        db (db): - original db connection
        AsyncModel (class): - parent class to create peewee models
        aio (class): - namespace of some CRUD operation
        SelectQuery (peewee.SelectQuery) : - select query
        UpdateQuery (peewee.UpdateQuery) : - update query
        InsertQuery (peewee.InsertQuery) : - insert query
        DeleteQuery (peewee.DeleteQuery) : - delete query
    """

    SelectQuery = SelectQuery
    UpdateQuery = UpdateQuery
    InsertQuery = InsertQuery
    DeleteQuery = DeleteQuery

    def __init__(self, dburl:str=None):
        super().__init__(dburl)
