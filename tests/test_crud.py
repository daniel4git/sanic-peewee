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
以mysql作为例子
"""


import asyncio

import unittest
from tests.models import MysqlTestModelAlpha, MysqlTestModelBeta, MysqlUUIDTestModel
from tests import peewee_mysql


class TestCRUD(unittest.TestCase):
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

    async def create_alphas(self):
        await MysqlTestModelAlpha.aio.create(text="new")
        await MysqlTestModelAlpha.aio.create(text="123")
        await MysqlTestModelAlpha.aio.create(text="234")
        return True
    async def create_alpha(self,text):
        await self.db.aio.insert(MysqlTestModelAlpha,text=text)
        return True

    async def get_alpha(self,text):
        result = await MysqlTestModelAlpha.aio.get(text=text)
        return result

    async def select_alpha(self):
        result = await self.db.aio.select(self.db.SelectQuery(MysqlTestModelAlpha))
        return result

    async def count_alpha(self):
        result = await self.db.aio.count(MysqlTestModelAlpha.select())
        return result

    async def execute_select_alpha(self):
        result = await self.db.aio.execute(MysqlTestModelAlpha.select())
        return result

    async def update_alpha(self,old, new):
        await self.db.aio.update(

            self.db.UpdateQuery(MysqlTestModelAlpha, update = {"text":"new").where(MysqlTestModelAlpha.text == old))
        return True
    async def execute_update_alpha(self,old, new):
        await self.db.aio.execute(
            MysqlTestModelAlpha.update(text=new).where(MysqlTestModelAlpha.text == old))
        return True
    async def object_update_alpha(self,old, new):
        obj = await MysqlTestModelAlpha.aio.get(text=text)
        obj.text = new
        await self.db.update(obj)
        return True

    async def delete_alpha(self,text):
        await self.db.aio.delete(
            self.db.DeleteQuery(MysqlTestModelAlpha).where(MysqlTestModelAlpha.text == text))
        return True
    async def executedelete_alpha(self,text):
        await self.db.aio.execute(
            MysqlTestModelAlpha.delete().where(MysqlTestModelAlpha.text == text))
        return True
    async def object_delete_alpha(self,text):
        obj = await MysqlTestModelAlpha.aio.get(text=text)
        await self.db.delete(obj)
        return True

    def test_create_select_count(self):
        async def _test():
            rst = await self.create_alphas()
            assert rst,"create error"
            rsts = await self.select_alpha()
            assert set([i.text for i in rsts])== set(["new","123","234"])
            count = await self.count_alpha()
            assert count == 3
        self.run_with_databases(_test)

    def test_create_select_count_excrute(self):
        async def _test():
            rst = await self.create_alphas()
            assert rst,"create error"
            rsts = await self.execute_select_alpha()
            assert set([i.text for i in rsts])== set(["new","123","234"])
            count = await self.count_alpha()
            assert count == 3
        self.run_with_databases(_test)

    def test_insert_get_delete(self):
        async def _test():
            await self.create_alpha("get")
            rst = await self.get_alpha("get")
            assert rst.text == "get"
            await self.delete_alpha("get")
        self.run_with_databases(_test)

    def test_insert_get_delete_excute(self):
        async def _test():
            await self.create_alpha("get")
            rst = await self.get_alpha("get")
            assert rst.text == "get"
            await self.executedelete_alpha("get")
        self.run_with_databases(_test)

    def test_insert_get_delete_object(self):
        async def _test():
            await self.create_alpha("get")
            rst = await self.get_alpha("get")
            assert rst.text == "get"
            await self.object_delete_alpha("get")
        self.run_with_databases(_test)

    def test_update(self):
        async def _test():
            await self.create_alpha("update")
            rst1 = await self.get_alpha("update")
            await self.update_alpha("update","updated")
            rst2 = await self.get_alpha("updated")
            assert rst1.id ==rst2.id
            await self.delete_alpha("updated")
        self.run_with_databases(_test)

    def test_update_execute(self):
        async def _test():
            await self.create_alpha("update")
            rst1 = await self.get_alpha("update")
            await self.execute_update_alpha("update","updated")
            rst2 = await self.get_alpha("updated")
            assert rst1.id ==rst2.id
            await self.delete_alpha("updated")
        self.run_with_databases(_test)

    def test_update_object(self):
        async def _test():
            await self.create_alpha("update")
            rst1 = await self.get_alpha("update")
            await self.object_update_alpha("update","updated")
            rst2 = await self.get_alpha("updated")
            assert rst1.id ==rst2.id
            await self.delete_alpha("updated")
        self.run_with_databases(_test)
