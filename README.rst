.. raw:: html

   <!--
   @Author: Huang Sizhe
   @Date:   05-Apr-2017
   @Email:  hsz1273327@gmail.com
   @Last modified by:
   @Last modified time: 2017-04-06T00:35:59+08:00
   @License: MIT
   -->

sanic-peewee
============

sanic-peewee is a asyncpeewee orm extension for sanic

.. code:: python

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
        obj = await KeyValue.aio.create(key=key, text=value)
        return json({'object_id': obj.id})


    @app.route('/get')
    async def get(request):
        """
        Load all objects from database
        """
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
