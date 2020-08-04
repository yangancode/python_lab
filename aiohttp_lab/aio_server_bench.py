# coding: utf-8
# @date: 2020-08-03

"""
aiohttp 服务端压测
"""

import random
import time
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,  # 根据IP限制访问频率
    default_limits=["200 per day", "100 per minute"]  # 默认限制，一天最多访问200次，一分钟最多访问100次
)


# 使用默认的限制
@app.route('/')
def index():
    time.sleep(3)
    print('default limit' + str(random.randint(0, 100)))
    return 'hello world'


# 使用自定义限制
@app.route('/limit')
@limiter.limit("10 per day")
def custom_limit():
    time.sleep(3)
    print('custom limit' + str(random.randint(0, 100)))
    return 'hello world'


@app.route('/not_limit')
@limiter.exempt
def not_limit():
    time.sleep(3)
    print('not limit' + str(random.randint(0, 100)))
    return 'hello world'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
