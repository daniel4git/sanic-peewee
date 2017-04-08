# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe <huangsizhe>
@Date:   06-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   huangsizhe
@Last modified time: 08-Apr-2017
@License: MIT
@Description:
"""



import asyncio

import unittest
from tests.models import MysqlTestModelAlpha, MysqlTestModelBeta, MysqlUUIDTestModel
from tests import peewee_mysql


class TestTransaction(unittest.TestCase):
    models = [MysqlTestModelAlpha, MysqlTestModelBeta, MysqlUUIDTestModel]
    db = peewee_mysql
    @classmethod
    def setUpClass(cls, *args, **kwargs):
        """Configure database managers, create test tables.
        """
        cls.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(cls.loop)
    @classmethod
    def tearDownClass(cls, *args, **kwargs):
        """Remove all test tables and close connections.
        """

        cls.loop.run_until_complete(cls.db.close())
        cls.loop.close()

    def setUp(self):
        self.db.create_tables(self.models,safe=True)

    def tearDown(self):
        self.db.drop_tables(self.models,safe=True)

    def run_with_databases(self, test,):
        """Run test coroutine against available databases.
        """
        self.loop.run_until_complete(test())
    def test_atomic():
        
