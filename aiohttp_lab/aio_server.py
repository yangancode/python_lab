# coding: utf-8
# @date: 2020-08-03

"""
aiohttp 服务端用法
"""
import time
from aiohttp import web


# 处理query请求
async def handle_query(request):
    time.sleep(3)
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


# 处理json请求（接收和返回都使用json）
async def handle_json(request):
    json_data = await request.json()
    print('data', json_data)
    return web.json_response(data=json_data)


app = web.Application()
app.add_routes([web.get('/', handle_query),
                web.get('/{name}', handle_query),
                web.post('/json', handle_json),
                ])

if __name__ == '__main__':
    web.run_app(app, port=5000)
