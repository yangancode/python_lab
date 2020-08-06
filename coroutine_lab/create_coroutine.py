# coding: utf-8
# @date: 2020-08-05

"""
协程创建
"""

import asyncio


# async、await、yield、yield from 区别

# 创建协程第一种方式（基于async关键字）
async def cor_by_async(delay, text):
    await asyncio.sleep(delay)
    print(text)


# 创建协程的第二种方式（基于@asyncio.coroutine）
# 这种方式在Python3.8中废弃，在Python3.10中会被移除，官方建议使用async这种方式
# 这种方式是async/await 语法的前身, 它们是使用 yield from 语句创建的 Python 生成器，可以等待 Future 和其他协程。
@asyncio.coroutine
def cor_by_asyncio(delay, text):
    yield from asyncio.sleep(delay)
    print(text)


if __name__ == '__main__':
    # 运行协程第一种方式：asyncio.run
    async def main():
        print('start')
        await cor_by_async(1, 'hello')
        print('end')

    asyncio.run(main())

    # 运行协程的第二种方式：created_task
    async def main2():
        task1 = asyncio.create_task(cor_by_async(1, 'hello'))
        await task1

    asyncio.run(main2())
