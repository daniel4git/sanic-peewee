数据库的表操作
=========================


数据库的表操作是同步阻塞的,因此我们不会在app的请求中使用,而是在app运行loop前先进行处理.



创建表格
------------------------

创建表格使用.create_tables( model_classes:list<model>, log=log, safe=False)

safe表示是否在创建表前先检测是否已经存在

删除表格
------------------------

删除表格使用.drop_tables(self, model_classes, log=log, safe=False, cascade=False)

其中safe标识是否在删除前先检测是否存在,cascade则是表示是否关联删除
