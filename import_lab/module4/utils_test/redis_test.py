# coding: utf-8
# @date: 2020-04-04

"""

"""
import sys

# 注意这里替换成自己的路径
# sys.path.append('/xxx/import_lab')

print("path", sys.path)

from module4.utils import redis_client


def redis_test():
    redis_client.set('redis_key', 'test')


if __name__ == '__main__':
    redis_test()
