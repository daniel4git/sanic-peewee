# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
# @Last modified by:
# @Last modified time: 2017-04-05T22:35:15+08:00
@License: MIT
@Description:
"""
__all__=["AsyncManager"]

from peewee_async import Manager, execute
from functools import partial


class AsyncManager(Manager):
    """异步管理
    """

    def __init__(self, _model_class, *args, **kwargs):
        super(AsyncManager, self).__init__(*args, **kwargs)
        self._model_class = _model_class
        self.database.allow_sync = False

    def _do_fill(self, method, *args, **kwargs):
        _class_method = getattr(super(AsyncManager, self), method)
        pf = partial(_class_method, self._model_class)
        return pf(*args, **kwargs)

    def create(self, *args, **kwargs):
        """Create a new object saved to database.
        Example::
            await Class_.async.create(*args,**kwargs)
        """
        return self._do_fill('create', *args, **kwargs)

    def get(self, *args, **kwargs):
        """Get the model instance.
        :param source_: model or base query for lookup
        Example::
            async def my_async_func():
                obj1 = await Class_.async.get(MyModel, id=1)
                obj2 = await Class_.async.get(MyModel, MyModel.id == 1)
                obj3 = await Class_.async.get(MyModel.select().where(MyModel.id == 1))
        All will return `MyModel` instance with `id = 1`
        """
        return self._do_fill('get', *args, **kwargs)

    def get_or_create(self,defaults=None, **kwargs):
        """Try to get an object or create it with the specified defaults.
        Return 2-tuple containing the model instance and a boolean
        indicating whether the instance was created.
        """
        return self._do_fill('get_or_create', *args, **kwargs)

    def create_or_get(self, **kwargs):
        """Try to create new object with specified data. If object already
        exists, then try to get it by unique fields.
        """
        return self._do_fill('create_or_get', *args, **kwargs)

    def execute(self, query):
        return execute(query)
