# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
@Author: Huang Sizhe <huangsizhe>
@Date:   01-Apr-2017
@Email:  hsz1273327@gmail.com
@Last modified by:   Huang Sizhe
@Last modified time: 05-Apr-2017
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



try:
    DB.create_tables(["KeyValue"])
except:
    print("table Exist")

DB.set_allow_sync(False)
@app.route('/post/<key>/<value>')
async def post(request, key, value):
    """
    Save get parameters to database
    """
    obj = await KeyValue.objects.new(key=key, text=value)
    return json({'object_id': obj.id})


@app.route('/get')
async def get(request):
    """
    Load all objects from database
    """
    all_objects = await KeyValue.objects.execute(KeyValue.select())
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
