# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   07-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 08-Apr-2017
@License: MIT
@Description:

测试需要自己先创建数据库

pg: `createdb test_pool`

然后ext_pool需要安装一个插件hstore

psql test_ext_pool -c 'create extension hstore;

所有数据库都安装:

psql template1 -c 'create extension hstore;'


"""
from sanic_peewee import Peewee
from sanic.config import Config


class FakeSanis:

    def __init__(self):
        self.config = Config()


DBURLS = {
    'postgres': "postgresql://{user}:{password}@{host}:{port}/{database}".format(
        database='test_sql',
        port=5432,
        host='127.0.0.1',
        user='huangsizhe',#postgres
        password='',#hsz881224
    ),
    'postgres-ext': "postgresqlext://{user}:{password}@{host}:{port}/{database}".format(
        database='test_ext',
        port=5432,
        host='127.0.0.1',
        user='huangsizhe',#postgres
        password='',#hsz881224
    ),
    'postgres-pool': "postgresql+pool://{user}:{password}@{host}:{port}/{database}?max_connections={max_connections}".format(
        database='test_pool',
        port=5432,
        host='127.0.0.1',
        user='huangsizhe',#postgres
        password='',#hsz881224
        max_connections=20
    ),
    'postgres-pool-ext': "postgresqlext+pool://{user}:{password}@{host}:{port}/{database}?max_connections={max_connections}".format(
        database='test_ext_pool',
        port=5432,
        host='127.0.0.1',
        user='huangsizhe',#postgres
        password='',#hsz881224
        max_connections=20
    ),
    'mysql': "mysql://{user}:{password}@{host}:{port}/{database}".format(
        database='test_sql',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224'
    ),
    'mysql-pool': "mysql+pool://{user}:{password}@{host}:{port}/{database}?max_connections={max_connections}".format(
        database='test_pool',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224',
        max_connections=20
    )
}


app_mysql = FakeSanis()
peewee1 = Peewee(DBURLS.get("mysql"))
peewee_mysql = peewee1(app_mysql)

app_mysql_pool = FakeSanis()
app_mysql_pool.config.DB_URL = DBURLS.get("mysql-pool")
peewee2 = Peewee()
peewee_mysql_pool = peewee2(app_mysql_pool)

app_postgresql = FakeSanis()
peewee3 = Peewee(DBURLS.get("postgres"))
peewee_postgresql = peewee3(app_postgresql)

app_postgresql_pool = FakeSanis()
app_postgresql_pool.config.DB_URL = DBURLS.get("postgres-pool")
peewee4 = Peewee()
peewee_postgresql_pool = peewee4(app_postgresql_pool)


app_postgres_ext = FakeSanis()
peewee5 = Peewee(DBURLS.get("postgres-ext"))
peewee_postgres_ext = peewee5(app_postgres_ext)

app_postgres_ext_pool = FakeSanis()
app_postgres_ext_pool.config.DB_URL = DBURLS.get("postgres-pool-ext")
peewee6 = Peewee()
peewee_postgres_ext_pool = peewee6(app_postgres_ext_pool)
