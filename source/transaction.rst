事务操作
===========================

db.async_atomic是实现原子操作的命令,他使用 async with 关键字处理异步上下文

例子: ::

    obj1 = await MysqlUUIDTestModel.aio.create(text='FOO')
    obj2 = await MysqlUUIDTestModel.aio.create(text='BAR')
    obj3 = await MysqlUUIDTestModel.aio.create(text='FOOBAR')
    obj1_id = obj1.id
    obj2_id = obj2.id
    obj3_id = obj3.id
    async with self.db.async_atomic():
        obj1.text = 'foo'
        obj2.text = 'bar'
        obj3.text = 'foobar'
        await self.db.aio.update(obj1)
        await self.db.aio.update(obj2)
        await self.db.aio.update(obj3)
