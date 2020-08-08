# coding: utf-8
# @date: 2020-08-07

"""
多进程数据共享

数据共享的场景:
"""

# from multiprocessing import Process, Manager
#
#
# # 参数中，传递了一个用于多进程之间数据共享的特殊字典（能否借鉴Go的channel思想？）
# def func(i: int, d: dict):
#     d[i] = i + 100
#     print(d.values())
#
#
# # 在主进程中创建特殊字典
# m = Manager()
# d = m.dict()
#
# for i in range(5):
#     # 让子进程去修改主进程的特殊字典
#     p = Process(target=func, args=(i, d))
#     p.start()
#
# p.join()


from multiprocessing import Process, Manager

# 创建一个共享数据的列表，或者说进程通信的列表
manager = Manager()
share_list = manager.list()

process_list = []


def foo(i):
    # 向列表中加入当前的进程序列号
    share_list.append(i)
    print('say hi', share_list)


for i in range(10):
    p = Process(target=foo, args=(i,))
    process_list.append(p)

for p in process_list:
    p.start()

for p2 in process_list:
    p2.join()

print('ending', share_list)
