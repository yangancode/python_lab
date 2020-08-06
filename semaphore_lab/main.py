# coding: utf-8
# @date: 2020-08-04

"""
信号量测试
"""

import time

import threading

# 信号计数器Semaphore，可以限制一个时间点的线程数量
# Semaphore 主要通过两个函数实现，acquire() 和 release()
# 执行acquire()的时候，会判断计数器的值是否大于0，大于0直接获得锁，且值减一；如果值小于0，则阻塞，直到执行release()释放锁，计数器值加一
sl = threading.Semaphore(5)


# 使用普通方式加锁
def foo():
    # 计数器获得锁 (获得锁的时候会判断计数器的值是否小于0，小于0则阻塞，直到线程释放锁，值大于0)
    sl.acquire()
    time.sleep(2)
    print('ok', time.ctime())
    # 计数器释放锁
    sl.release()


for i in range(20):
    tl = threading.Thread(target=foo, args=())
    tl.start()
    print('index', i)


# 使用上下文的方式加锁
def foo2():
    with sl:
        time.sleep(3)
        print('ok', time.ctime())


for i in range(20):
    tl = threading.Thread(target=foo2, args=())
    tl.start()
