"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 05-Apr-2017
@License: MIT
@Description:
"""
__all__=["select","prefetch","scalar","atomic","savepoint","transaction","count",
"create","delete","get","insert","update",
"Peewee","database"]
# 搜索
from peewee_async import select
# 数据预取
from peewee_async import prefetch
# 相当于select(),但数据为一个整体
from peewee_async import scalar
"""事务操作,配合`async with`使用
"""
from peewee_async import atomic # 原子操作
from peewee_async import savepoint  # 保存点
from peewee_async import transaction # 事务

# 结果计数,相当于`.count()`
from peewee_async import count
"""增删改查"""
from peewee_async import create_object as create
from peewee_async import delete_object as delete
from peewee_async import get_object as get
from peewee_async import insert
from peewee_async import update_object as update

from .core import database,Core
from .mixins import TableHandlerMixin


class Peewee(Core,TableHandlerMixin,TransactionhandlerMixin):
    def __init__(self, db=None):
        super().__init__(db)
