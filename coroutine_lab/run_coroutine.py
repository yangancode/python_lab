# coding: utf-8
# @date: 2020-08-06

"""
协程的流程
"""

import asyncio
import time

start = time.time()


# 协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


# 协程对象
coroutine1 = do_some_work(2)
coroutine3 = do_some_work(4)

# 将协程转成task，并添加到一个任务列表
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine3)
]

# 创建一个事件循环
loop = asyncio.get_event_loop()
# 等待所有任务运行完成
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print("time_consume:", time.time() - start)
