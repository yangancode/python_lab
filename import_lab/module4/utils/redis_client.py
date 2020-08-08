# coding: utf-8
# @date: 2020-04-04

"""

"""
import redis


pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=1)
redis_client = redis.StrictRedis(connection_pool=pool)
