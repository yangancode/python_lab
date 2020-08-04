# coding: utf-8
# @date: 2020-08-03

"""
压测程序1
"""
import asyncio
import aiohttp


async def hello(url, semaphore):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.read()
                print(data)
                return data


async def run():
    url = 'http://127.0.0.1:5000/'
    # 限制并发量为5 (由于服务端有3秒的时间限制，所以可以看到每隔3秒打印一次，每次5行，所以semaphore确实限制了访问速率)
    semaphore = asyncio.Semaphore(5)
    to_get = [hello(url.format(), semaphore) for _ in range(100)]  # 总共1000任务
    await asyncio.wait(to_get)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    loop.close()
