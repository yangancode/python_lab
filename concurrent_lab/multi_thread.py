# coding: utf-8
# @date: 2020-08-08

"""
线程池
"""

import threading
from concurrent.futures import ThreadPoolExecutor


# 注：这里是新起一个进程运行
def task(task_id):
    import os, time
    time.sleep(2)
    print('子进程开始执行，父进程id: {0}，子进程id: {1}，任务id：{2}'.format(os.getppid(), os.getpid(), task_id))
    return os.getpid()


def create_thread_by_future():
    t = ThreadPoolExecutor(3)

    task_list = []
    for i in range(9):
        obj = t.submit(task, i)
        task_list.append(obj)

    t.shutdown()
    print([obj.result() for obj in task_list])


# 普通多线程
def create_thread_by_threading():
    threads = []
    for i in range(9):
        threads.append(threading.Thread(target=task, args=(i, )))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


# 通过信号量实现线程池
sl = threading.Semaphore(3)


def task_new(task_id):
    import os, time
    # 加锁
    sl.acquire()
    time.sleep(2)
    print('子进程开始执行，父进程id: {0}，子进程id: {1}，任务id：{2}'.format(os.getppid(), os.getpid(), task_id))
    # 释放锁
    sl.release()
    return os.getpid()


def create_thread_by_semaphore():
    threads = []
    for i in range(9):
        threads.append(threading.Thread(target=task_new, args=(i, )))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    import time

    start = time.time()
    # create_thread_by_future()
    # create_thread_by_threading()
    create_thread_by_semaphore()
    print('cost', time.time() - start)
