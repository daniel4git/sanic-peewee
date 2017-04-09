<!--
@Author: Huang Sizhe
@Date:   05-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   huangsizhe
@Last modified time: 08-Apr-2017
@License: MIT
-->



# sanic-peewee

sanic-peewee 是一个基于async-peewee的sanic扩展旨在为sanic提供便捷的异步orm操作

sanic-peewee is a async_peewee orm extension for sanic,
I hope users can deal with the database simplely and efectively when using sanic.

本项目受启发于官方文档的[例子](https://github.com/channelcat/sanic/blob/master/examples/sanic_peewee.py)
this project's idea is from [the examples of sanic's official documents](https://github.com/channelcat/sanic/blob/master/examples/sanic_peewee.py)

## 特点 Features

+ 接近阻塞版peewee的操作接口 // a peewee API similar to peewee's standard, blocking API.
+ 支持3.5版本以上的 // support for async/await (PEP 492) constructs
+ 使用简洁的database url // use database url (peewee's playhose)
+ 支持异步的事务,连接池以及peewee的pg扩展 // support transaction, pool and pg's ext (peewee-async)
+ 阻塞的处理table的增删,异步的处理数据的增删改查操作 //sync api for creating and delecting tables,async api for GRUD data.


## 依赖 Requirements

1. aiomysql>=0.0.9
2. aiopg>=0.13.0
3. peewee>=2.9.1
4. peewee-async>=0.5.7
5. psycopg2>=2.7.1
6. PyMySQL>=0.7.10
7. sanic>=0.4.1

## 安装 Installation

    pip install sanic-peewee

## 文档 Document

[sanic-peewee](https://sanic-extensions.github.io/sanic-peewee/)

## 测试 Test

测试需要在数据库中新建几张对应的表,并且在测试代码中填上数据库的账号密码

本项目测试覆盖率88%

测试命令:

```shell
python3 -m unittest discover -v -s ./tests
```

代码覆盖:

```shell
coverage3 run --source=sanic_peewee  -m unittest discover -v -s ./tests
coverage3 html -d htmlcov
```

## 例子 Example

```python
from sanic import Sanic
from sanic.response import text,json
from sanic_peewee import Peewee,select
from peewee import CharField, TextField

app = Sanic(__name__)
dburl = "mysql://{user}:{password}@{host}:{port}/{database}".format(
    database='test1',
    port=3306,
    host='127.0.0.1',
    user='root',
    password='hsz881224'
)
peewee = Peewee(dburl)
db = peewee(app)


class KeyValue(db.AsyncModel):
    key = CharField(max_length=40, unique=True)
    text = TextField(default='')



db.create_tables([KeyValue])



@app.route('/post/<key>/<value>')
async def post(request, key, value):
    """
    Save get parameters to database
    """
    obj = await KeyValue.aio.create(key=key, text=value)# use the model's async object to manage the query
    return json({'object_id': obj.id})


@app.route('/get')
async def get(request):
    """
    Load all objects from database
    """
    # use the sanic_peewee object's async api
    all_objects = await db.aio.select(db.SelectQuery(KeyValue))

    serialized_obj = []
    for obj in all_objects:
        serialized_obj.append({
            'id': obj.id,
            'key': obj.key,
            'value': obj.text}
        )

    return json({'objects': serialized_obj})


@app.route("/")
async def test(request):
    return text('Hello world!')

app.run(host="0.0.0.0", port=8000, debug=True)
```
