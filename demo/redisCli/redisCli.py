# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 19:33
# @Author  : Ian Leto
# @File    : redisCli.py
# 干啥的    :

import redis
import datetime
import time

cli = redis.Redis(host='39.108.86.208', port=6379, db=0)
cli.set("admin", 'IanLeto')


def redis_consumer():
    while 1 == 1:
        print(cli.lpop("tList"))


def redis_producer():
    count = 0
    while 1 == 1:
        time.sleep(1)
        count += 1
        print(cli.lpush("tList", count))


if __name__ == '__main__':
    redis_consumer()
    redis_producer()
