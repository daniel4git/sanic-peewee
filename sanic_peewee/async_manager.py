# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 06-Apr-2017
@License: MIT
@Description:
"""
__all__ = ["AsyncManager"]

from peewee_async import Manager, execute
from functools import partial


class AsyncManager(Manager):
    """
    继承自peewee_async的异步管理工具,此处用来构造model父类所携带的aio对象

    async manager from peewee_async.Manager.here we use it in constructing the aio object in model's partent class
    """

    def __init__(self, _model_class, *args, **kwargs):
        """构造函数

        Parameters:
            _model_class (class): - 参数用来绑定实例到model类的aio对象
        """
        super(AsyncManager, self).__init__(*args, **kwargs)
        self._model_class = _model_class
        self.database.allow_sync = False

    def _do_fill(self, method, *args, **kwargs):
        """利用偏函数将方法第一位的类对象绑定为自身所在的类

        Parameters:
            _model_class (class): - 参数用来绑定实例到model类的aio对象

        Return:
            object: - 将方法对应偏函数运行,结果看所运行的函数结果是什么
        """
        _class_method = getattr(super(AsyncManager, self), method)
        pf = partial(_class_method, self._model_class)
        return pf(*args, **kwargs)

    def create(self, *args, **kwargs):
        """Create a new object saved to database.

        Parameters:
            args (list): - 用来创建数据的参数
            kwargs (dict): - 用来创建数据的参数

        Return:
            object: - 将方法对应偏函数运行,结果看所运行的函数结果是什么

        Example:
            await <Class>.aio.create(\*args,\*\*kwargs)
        """
        return self._do_fill('create', *args, **kwargs)

    def get(self, *args, **kwargs):
        """Get the model instance.

        Parameters:
            args  (list): - 用来标识要get的数据的参数
            kwargs (dict): - 用来标识要get的数据的参数

        Return:
            object: - 获取的对应object

        Example:
            async def my_async_func():
                obj1 = await <Class>.aio.get(MyModel, id=1)
                obj2 = await <Class>.aio.get(MyModel, MyModel.id == 1)
                obj3 = await <Class>.aio.get(MyModel.select().where(MyModel.id == 1))

        All will return MyModel instance with id = 1
        """
        return self._do_fill('get', *args, **kwargs)

    def get_or_create(self, defaults=None, **kwargs):
        """Try to get an object or create it with the specified defaults.
        Return 2-tuple containing the model instance and a boolean
        indicating whether the instance was created.
        
        Parameters:
            defaults (dict): - 默认创建的对象参数

        Return:
            object: - 将方法对应偏函数运行,结果看所运行的函数结果是什么
        """
        return self._do_fill('get_or_create', defaults=defaults, **kwargs)

    def create_or_get(self, **kwargs):
        """Try to create new object with specified data. If object already
        exists, then try to get it by unique fields.

        Parameters:
            kwargs (dict): - 创建或者获取对象所用到的字段

        Return:
            object: - 将方法对应偏函数运行,结果看所运行的函数结果是什么


        """
        return self._do_fill('create_or_get', **kwargs)

    def execute(self, query):
        """
        Parameters:
            query (peewee.Query): - 要执行的请求

        Return:
            object: - 将方法对应偏函数运行,结果看所运行的请求结果是什么

        """
        return execute(query)
