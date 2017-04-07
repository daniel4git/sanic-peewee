# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   07-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   huangsizhe
@Last modified time: 07-Apr-2017
@License: MIT
@Description:
"""

import uuid

from tests import peewee_mysql, peewee_mysql_pool, peewee_postgresql, peewee_postgresql_pool, peewee_postgres_ext, peewee_postgres_ext_pool
import peewee
# mysql
ModelMysql = peewee_mysql.AsyncModel
class MysqlTestModelAlpha(ModelMysql):
    text = peewee.CharField()


class MysqlTestModelBeta(ModelMysql):
    alpha = peewee.ForeignKeyField(MysqlTestModelAlpha, related_name='betas')
    text = peewee.CharField()


class MysqlUUIDTestModel(ModelMysql):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

# mysqlpool

Modelmysql_pool = peewee_mysql_pool.AsyncModel


class Mysql_PoolTestModelAlpha(Modelmysql_pool):
    text = peewee.CharField()


class Mysql_PoolTestModelBeta(Modelmysql_pool):
    alpha = peewee.ForeignKeyField(
        Mysql_PoolTestModelAlpha, related_name='betas')
    text = peewee.CharField()


class Mysql_PoolUUIDTestModel(Modelmysql_pool):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

# postgresql
Modelpostgresl = peewee_postgresql.AsyncModel


class postgresTestModelAlpha(Modelpostgresl):
    text = peewee.CharField()


class postgresTestModelBeta(Modelpostgresl):
    alpha = peewee.ForeignKeyField(
        postgresTestModelAlpha, related_name='betas')
    text = peewee.CharField()


class postgresUUIDTestModel(Modelpostgresl):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

# postgresql_pool

Modelpostgresql_pool = peewee_postgresql_pool.AsyncModel


class postgresql_poolTestModelAlpha(Modelpostgresql_pool):
    text = peewee.CharField()


class postgresql_poolTestModelBeta(Modelpostgresql_pool):
    alpha = peewee.ForeignKeyField(
        postgresql_poolTestModelAlpha, related_name='betas')
    text = peewee.CharField()


class postgresql_poolUUIDTestModel(Modelpostgresql_pool):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()


# postgresql
Modelpostgresl_ext = peewee_postgres_ext.AsyncModel


class postgres_extTestModelAlpha(Modelpostgresl_ext):
    text = peewee.CharField()


class postgres_extTestModelBeta(Modelpostgresl_ext):
    alpha = peewee.ForeignKeyField(
        postgres_extTestModelAlpha, related_name='betas')
    text = peewee.CharField()


class postgres_extUUIDTestModel(Modelpostgresl_ext):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()

# postgresql_pool

Modelpostgresql_ext_pool = peewee_postgres_ext_pool.AsyncModel


class postgresql_ext_poolTestModelAlpha(Modelpostgresql_ext_pool):
    text = peewee.CharField()


class postgresql_ext_poolTestModelBeta(Modelpostgresql_ext_pool):
    alpha = peewee.ForeignKeyField(
        postgresql_ext_poolTestModelAlpha, related_name='betas')
    text = peewee.CharField()


class postgresql_ext_poolUUIDTestModel(Modelpostgresql_ext_pool):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    text = peewee.CharField()
