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
import unittest

from tests import peewee_mysql, peewee_mysql_pool, peewee_postgresql, peewee_postgresql_pool, peewee_postgres_ext, peewee_postgres_ext_pool


from tests.models import Mysql_PoolTestModelAlpha, Mysql_PoolTestModelBeta, Mysql_PoolUUIDTestModel
from tests.models import MysqlTestModelAlpha, MysqlTestModelBeta, MysqlUUIDTestModel

from tests.models import postgresTestModelAlpha, postgresTestModelBeta, postgresUUIDTestModel
from tests.models import postgresql_poolTestModelAlpha, postgresql_poolTestModelBeta, postgresql_poolUUIDTestModel

from tests.models import postgres_extTestModelAlpha, postgres_extTestModelBeta, postgres_extUUIDTestModel
from tests.models import postgresql_ext_poolTestModelAlpha, postgresql_ext_poolTestModelBeta, postgresql_ext_poolUUIDTestModel


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_mysqltable(self):

        assert peewee_mysql.create_tables(
            [MysqlTestModelAlpha, MysqlTestModelBeta, MysqlUUIDTestModel])
        assert peewee_mysql.drop_tables([MysqlTestModelAlpha, MysqlTestModelBeta,MysqlUUIDTestModel])

    def test_mysqlt_poolable(self):

        assert peewee_mysql_pool.create_tables(
            [Mysql_PoolTestModelAlpha, Mysql_PoolTestModelBeta, Mysql_PoolUUIDTestModel])
        assert peewee_mysql_pool.drop_tables([Mysql_PoolTestModelAlpha, Mysql_PoolTestModelBeta, Mysql_PoolUUIDTestModel])
