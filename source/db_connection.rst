连接数据库
=================================

sanic-peewee是 .. peewee-async: https://github.com/05bit/peewee-async 的封装,
它支持的数据库目前有` PostgreSQL`和`MySQL`两种.
其中`PostgreSQL`支持的更加好一些,两种数据库都可以使用池连接,pg也可以使用peewee中的扩展连接.

要使用pg,需要额外安装`aiopg`,要使用mysql则需要额外安装`aiomysql`.

他们的池连接方式可以设定参数`max_connections`也就是最大连接数.

这些信息都需要在database url中体现


使用 Database Url
-----------------------------------

sanic-peewee只能使用Database Url来定义连接.它可以在程序内定义,也可以在app的config中定义.
这么做的好处是减少参数数目,统一的格式也更加利于管理

下面是给出的合法的dburl:

+ postgresql://user:password@host:port/dbname
+ mysql://user:password@host:port/dbname
+ mysql+pool://user:password@host:port/dbname?max_connections=20
+ postgresql+pool://user:passwd@ip:port/dbname?max_connections=20
+ postgresqlext://user:passwd@ip:port/dbname
+ postgresqlext+pool://user:passwd@ip:port/dbname?max_connections=20


初始化扩展和绑定sanic app
------------------------------------

我们的扩展初始化可以带database url作为参数;如果不带,
那么他就会在之后绑定app的时候通过查找app.config.DB_URL来初始化连接的数据库.

方法一,使用dburl作为参数初始化: ::


    from sanic import Sanic
    from sanic_peewee import Peewee
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



方法二,使用app.config.DB_URL作为参数初始化: ::


        from sanic import Sanic
        from sanic_peewee import Peewee
        app = Sanic(__name__)
        app.config.DB_URL = "mysql://{user}:{password}@{host}:{port}/{database}".format(
            database='test1',
            port=3306,
            host='127.0.0.1',
            user='root',
            password='hsz881224'
        )
        peewee = Peewee()
        db = peewee(app)
