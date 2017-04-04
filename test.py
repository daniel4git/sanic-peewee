# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe <huangsizhe>
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   huangsizhe
@Last modified time: 01-Apr-2017
@License: MIT
@Description:
"""

from sanic import Sanic
from sanic.response import text
from sanic_peewee import Peewee, database

app = Sanic(__name__)
db = database(dbtype="mysql",
              database='test',
              host='127.0.0.1',
              user='root',
              password='hsz881224')
peewee=Peewee(db)
DB = peewee(app)

class KeyValue(DB.AsyncModel):
    key = peewee.CharField(max_length=40, unique=True)
    text = peewee.TextField(default='')

DB.


@app.route("/")
async def test(request):
    return text('Hello world!')

app.run(host="0.0.0.0", port=8000, debug=True)
