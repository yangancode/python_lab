# coding: utf-8
# @date: 2020-08-08

"""
数据库连接池
"""

import pymysql
from DBUtils.PersistentDB import PersistentDB
from DBUtils.PooledDB import PooledDB


# 为每个线程创建一个连接，线程即使调用了close方法，也不会关闭，只是把连接重新放到连接池，供自己线程再次使用。
# 当线程终止时，连接自动关闭。（如果线程比较多还是会创建很多连接，推荐使用模式二）
class BaseModel:
    def __init__(self):
        mysql_pool = PooledDB(
            # 使用的mysql驱动
            creator=pymysql,
            host='127.0.0.1',
            port='root',
            user='root',
            password='root',
            database='py_test',
            charset='utf8mb4',
            # 连接池允许的最大连接数
            maxconnections=10,
            # 初始化时，连接池中至少创建的空闲的链接
            mincached=2,
            # 连接池中最多共享的连接数量
            maxshared=3,
            # 一个连接最多被重复使用的次数，None表示无限制
            maxusage=None,

        )
        self.db_conn = mysql_pool.connection()

        # 设置返回的数据类型为dict，而不是tuple
        self.cursor = self.db_conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db_conn.close()


"""
模式二：创建一批连接到连接池，供所有线程共享使用，使用完毕后再放回到连接池。（由于pymysql、MySQLdb等threadsafety值为1，所以该模式连接池中的连接会被所有线程共享。
"""


class PersistBaseModel:
    def __init__(self):
        mysql_pool = PersistentDB(
            # 使用的mysql驱动
            creator=pymysql,
            host='127.0.0.1',
            port='root',
            user='root',
            password='root',
            database='py_test',
            charset='utf8mb4',
            # 一个连接最多被重复使用的次数，None表示无限制
            maxusage=None,
        )
        self.db_conn = mysql_pool.connection()

        # 设置返回的数据类型为dict，而不是tuple
        self.cursor = self.db_conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db_conn.close()
