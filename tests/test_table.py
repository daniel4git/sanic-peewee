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
import unittest

from . import peewee_mysql, peewee_mysql_pool, peewee_postgresql, peewee_postgresql_pool, peewee_postgres_ext, peewee_postgres_ext_pool

class TestStringMethods(unittest.TestCase):
    dbs = [peewee_mysql. peewee_mysql_pool, peewee_postgresql, peewee_postgresql_pool, peewee_postgres_ext, peewee_postgres_ext_pool]
    def setUp(self):



    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
