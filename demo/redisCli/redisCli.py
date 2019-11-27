# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 19:33
# @Author  : Ian Leto
# @File    : redisCli.py
# 干啥的    :

import redis
import time
from redis.sentinel import Sentinel

cli = redis.Redis(host='39.108.86.208', port=6379, db=0)
cli.set("admin", 'IanLeto')


def new_redis_sentinel() -> redis.sentinel:
    return Sentinel([('39.108.86.208', 26379)])


def new_redis_client(host: str = '39.108.86.208', port: int = 6379, db: int = 0) -> redis.Redis:
    return redis.Redis(host=host, port=port, db=db)


def redis_consumer():
    while 1 == 1:
        print(cli.lpop("tList"))


def redis_producer():
    count = 0
    while 1 == 1:
        time.sleep(1)
        count += 1
        print(cli.lpush("tList", count))
