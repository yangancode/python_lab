# coding: utf-8
# @date: 2020-08-04

"""
压测程序2
"""
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as resp:
        if resp.status != 200:
            resp.raise_for_status()
        data = await resp.text()
        print(data)
        return data


async def fetch_multi(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    # gather: 搜集所有future对象，并等待返回
    results = await asyncio.gather(*tasks)
    return results


async def main():
    # 限制并发
    urls = ["http://127.0.0.1:5000/" for _ in range(100)]
    conn = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=conn) as session:
        # 获取返回值
        await fetch_multi(session, urls)


if __name__ == '__main__':
    asyncio.run(main())
