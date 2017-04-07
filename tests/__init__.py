# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   07-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 07-Apr-2017
@License: MIT
@Description:
"""
from sanic_peewee import Peewee


class Config:
    def __init__(self,**kws):
        if kws:
            for k,v in kws.items():
                self.k = v


class FakeSanis:
    def __init__(self):
        self.config = Config()


DBURLS = {
    'postgres':"postgresql://{user}:{password}@{host}:{port}/{database}".format(
        database='test_sql',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224'
    ),
    'postgres-ext':"postgresqlext://{user}:{password}@{host}:{port}/{database}".format(
        database='test_ext',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224'
    ),
    'postgres-pool':"postgresql+pool://{user}:{password}@{host}:{port}/{database}?max_connections={max_connections}&stale_timeout={stale_timeout}".format(
        database='test_pool',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224',
        max_connections=20,
        stale_timeout=300
    ),
    'postgres-pool-ext':"postgresqlext+pool://{user}:{password}@{host}:{port}/{database}?max_connections={max_connections}&stale_timeout={stale_timeout}".format(
        database='test_ext_pool',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224',
        max_connections=20,
        stale_timeout=300
    ) ,
    'mysql':"mysql://{user}:{password}@{host}:{port}/{database}".format(
        database='test_sql',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224'
    ),
    'mysql-pool':"mysql+pool://{user}:{password}@{host}:{port}/{database}?max_connections={max_connections}&stale_timeout={stale_timeout}".format(
        database='test_pool',
        port=3306,
        host='127.0.0.1',
        user='root',
        password='hsz881224',
        max_connections=20,
        stale_timeout=300
    )
}

app_mysql = FakeSanis(DBURLS.get("mysql"))
peewee_mysql = Peewee(app_mysql)

app_mysql_pool = FakeSanis()
app2.config.DB_URL = DBURLS.get("mysql-pool")
peewee_mysql_pool = Peewee(app_mysql_pool)

app_postgresql = FakeSanis(DBURLS.get("postgres"))
peewee_postgresql = Peewee(app_postgresql)

app_postgresql_pool = FakeSanis()
app2.config.DB_URL = DBURLS.get("postgres-pool")
peewee_postgresql_pool = Peewee(app_postgresql_pool)


app_postgres_ext = FakeSanis(DBURLS.get("postgres-ext"))
peewee_postgres_ext = Peewee(app_postgres_ext)

app_postgres_ext_pool = FakeSanis()
app2.config.DB_URL = DBURLS.get("postgres-ext-pool")
peewee_postgres_ext_pool = Peewee(app_postgres_ext_pool)
