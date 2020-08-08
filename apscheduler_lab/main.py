# coding: utf-8
# @date: 2019-12-01

"""
apscheduler库使用demo

"""

import time

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime


def my_task(params):
    print("params is: ", params)


def background_scheduler_test():
    """后台运行"""
    url = 'mysql+pymysql://root:123456@127.0.0.1:33306/mysqltest?charset=utf8mb4'

    executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5)
            }

    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }

    conf = {
            "host": "127.0.0.1",
            "port": 6379,
            "db": 0,
            "max_connections": 10
          }

    # 后台调度器，适用于非阻塞的情况，调度器会在后台独立运行
    scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults)
    # 将任务存储在mysql(会报错)
    # 需安装sqlalchemy库
    scheduler.add_jobstore('sqlalchemy', url=url, tablename='schedule_job')
    scheduler.add_job(func=my_task, trigger='interval', seconds=3, args=["db task"])
    # 将任务存储在redis
    # scheduler.add_jobstore(jobstore="redis", **conf)
    scheduler.start()
    while True:
        time.sleep(20)
        break


def block_scheduler_test():
    # 阻塞式调度器
    scheduler = BlockingScheduler()
    # 每隔6秒执行一次，立即执行
    scheduler.add_job(func=my_task, trigger="interval", seconds=6, args=["do right now！"], next_run_time=datetime.now())
    # 每隔5秒后执行，等待6秒后执行
    scheduler.add_job(func=my_task, trigger="interval", seconds=6, args=["do later"])
    # 阻塞函数
    scheduler.start()


if __name__ == '__main__':
    # block_scheduler_test()
    background_scheduler_test()


