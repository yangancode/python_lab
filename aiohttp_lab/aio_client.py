# coding: utf-8
# @date: 2020-08-02

"""
aiohttp 客户端用法
"""
import time
import asyncio, aiohttp


# # ########### 1.请求单个URL
# async def fetch(session, url):
#     # with语句保证在处理session的时候，总是能正确的关闭它
#     async with session.get(url) as resp:
#         # 1.如果想要得到结果，则必须使用await关键字等待请求结束，如果没有await关键字，得到的是一个生成器
#         # 2.text()返回的是字符串的文本，read()返回的是二进制的文本
#         data = await resp.text()
#         print('data', data)
#         return data
#
#
# async def run():
#     async with aiohttp.ClientSession() as session:
#         html_data = await fetch(session, "http://127.0.0.1:5000/")
#         print('html', html_data)
#
#
# if __name__ == '__main__':
#     # 创建一个事件循环
#     loop = asyncio.get_event_loop()
#     # run函数是一个异步函数，同时也是一个future对象，run_until_complete会等待future对象结束后才退出
#     loop.run_until_complete(run())


# ########### 2.请求多个URL，但是会重复创建session
# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             data = await resp.text()
#             return data
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = []  # I'm using test server localhost, but you can use any url
#     url = "http://127.0.0.1:5000/"
#     for i in range(10):
#         task = asyncio.ensure_future(fetch(url))
#         tasks.append(task)
#     # 得到返回结果
#     results = loop.run_until_complete(asyncio.wait(tasks))
#     for r in results[0]:
#         print('r', r.result())


# ########### 3.请求多个URL，但不会重复创建session
# async def fetch(session, url):
#     async with session.get(url) as resp:
#         if resp.status != 200:
#             resp.raise_for_status()
#         data = await resp.text()
#         return data
#
#
# async def fetch_multi(session, urls):
#     tasks = []
#     for url in urls:
#         task = asyncio.create_task(fetch(session, url))
#         tasks.append(task)
#     # gather: 搜集所有future对象，并等待返回
#     results = await asyncio.gather(*tasks)
#     return results
#
#
# async def main():
#     # 限制并发
#     urls = ["http://127.0.0.1:5000/" for _ in range(10)]
#     async with aiohttp.ClientSession() as session:
#         datas = await fetch_multi(session, urls)
#         print(datas)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())


# ########### 4.请求多个URL，错误做法
# async def fetch():
#     async with aiohttp.ClientSession() as session:
#         for i in range(1, 10):
#             url = "http://127.0.0.1:5000/"
#             async with session.get(url) as resp:
#                 data = await resp.text()
#                 print('data', data)
#                 # 加上return语句只会执行一次
#                 # return data
#
#
# if __name__ == '__main__':
#     # 创建一个事件循环
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(fetch())


# ########### 5.使用TCPConnector控制并发
# async def fetch(session, url):
#     async with session.get(url) as resp:
#         if resp.status != 200:
#             resp.raise_for_status()
#         data = await resp.text()
#         print('data', data + " " + time.ctime())
#         return data
#
#
# async def fetch_multi(session, urls):
#     tasks = []
#     for url in urls:
#         task = asyncio.create_task(fetch(session, url))
#         tasks.append(task)
#     # gather: 搜集所有future对象，并等待返回
#     results = await asyncio.gather(*tasks)
#     return results
#
#
# async def main():
#     urls = ["http://127.0.0.1:5000/" for _ in range(10)]
#     conn = aiohttp.TCPConnector(limit=3)
#     async with aiohttp.ClientSession(connector=conn) as session:
#         datas = await fetch_multi(session, urls)
#         print(datas)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# ########### 6.使用Semaphore控制并发
async def fetch(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.text()
                print('data', data + " " + time.ctime())
                return data


async def run():
    url = 'http://127.0.0.1:5000'
    semaphore = asyncio.Semaphore(2)  # 限制并发量为2
    to_get = [fetch(url, semaphore) for _ in range(10)]
    await asyncio.wait(to_get)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
