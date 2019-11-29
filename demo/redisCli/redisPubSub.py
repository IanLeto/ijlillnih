# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 19:51
# @Author  : Ian Leto
# @File    : redisPubSub.py
# 干啥的    : 发布/订阅
from demo.redisCli.redisCli import new_redis_client, new_redis_sentinel

sentinel = new_redis_sentinel()
sentinel.discover_master('mymaster')
print(sentinel.discover_master('mymaster'))
