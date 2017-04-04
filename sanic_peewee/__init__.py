"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   huangsizhe
@Last modified time: 01-Apr-2017
@License: MIT
@Description:
"""
__all__=["select","prefetch","scalar","atomic","savepoint","transaction","count",
"create_object","delete","delete_object","get_object","insert","update",
"update_object","Peewee","database"]
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
from peewee_async import create_object
from peewee_async import delete
from peewee_async import delete_object
from peewee_async import get_object
from peewee_async import insert
from peewee_async import update
from peewee_async import update_object

from core import database,Peewee
