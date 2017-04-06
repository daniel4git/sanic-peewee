.. sanic_peewee documentation master file, created by
   sphinx-quickstart on Thu Apr  6 15:40:55 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Sanic-peewee
========================================

sanic-peewee 是一个基于async-peewee的sanic扩展旨在为sanic提供便捷的异步orm操作

sanic-peewee is a async_peewee orm extension for sanic,
I hope users can deal with the database simplely and efectively when using sanic.


特点 Features
-----------------------------------------

+ 接近阻塞版peewee的操作接口 // a peewee API similar to peewee's standard, blocking API.
+ 支持3.5版本以上的 // support for async/await (PEP 492) constructs
+ 使用简洁的database url // use database url (peewee's playhose)
+ 支持异步的事务,连接池以及peewee的pg扩展 // support transaction, pool and pg's ext (peewee-async)
+ 阻塞的处理table的增删,异步的处理数据的增删改查操作 //sync api for creating and delecting tables,async api for GRUD data.


依赖 Requirements
------------------------------------------
1. aiomysql>=0.0.9
2. aiopg>=0.13.0
3. peewee>=2.9.1
4. peewee-async>=0.5.7
5. psycopg2>=2.7.1
6. PyMySQL>=0.7.10
7. sanic>=0.4.1

安装 Installation
-----------------------------------------

命令行中使用: ::

    pip install sanic-peewee

文档 Document
-----------------------------------------

.. toctree::
   :maxdepth: 3

   db_connection
   create_model
   tablehandler
   queryhandler
   transaction


接口详情 Api
------------------------------------------

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   sanic_peewee


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
