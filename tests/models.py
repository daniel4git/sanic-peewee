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
import uuid

from . import peewee_mysql, peewee_mysql_pool, peewee_postgresql, peewee_postgresql_pool, peewee_postgres_ext, peewee_postgres_ext_pool

################################################################################mysql
ModelMysql = peewee_mysql.AsyncModel


class MysqlTestModelAlpha(ModelMysql):
    text = peewee.CharField()


class MysqlTestModelBeta(ModelMysql):
    alpha = peewee.ForeignKeyField(MysqlTestModelAlpha, related_name='betas')
    text = peewee.CharField()

class MysqlUUIDTestModel(ModelMysql):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

##############################################################################mysqlpool

Modelmysql_pool=peewee_mysql_pool.AsyncModel

class Mysql_PoolTestModelAlpha(Modelmysql_pool):
    text = peewee.CharField()


class Mysql_PoolTestModelBeta(Modelmysql_pool):
    alpha = peewee.ForeignKeyField(Mysql_PoolTestModelAlpha, related_name='betas')
    text = peewee.CharField()

class Mysql_PoolUUIDTestModel(Modelmysql_pool):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

################################################################################postgresql
Modelpostgresl=peewee_postgres.AsyncModel

class postgresTestModelAlpha(Modelpostgresl):
    text = peewee.CharField()


class postgresTestModelBeta(Modelpostgresl):
    alpha = peewee.ForeignKeyField(postgresTestModelAlpha, related_name='betas')
    text = peewee.CharField()

class postgresUUIDTestModel(Modelpostgresl):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

################################################################################postgresql_pool

peewee_postgresql, peewee_postgresql_pool, peewee_postgres_ext, peewee_postgres_ext_pool
class MysqlTestModelAlpha(ModelMysql):
    text = peewee.CharField()


class MysqlTestModelBeta(ModelMysql):
    alpha = peewee.ForeignKeyField(MysqlTestModelAlpha, related_name='betas')
    text = peewee.CharField()

class MysqlUUIDTestModel(ModelMysql):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()
