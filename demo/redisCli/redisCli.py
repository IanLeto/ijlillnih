# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 19:33
# @Author  : Ian Leto
# @File    : redisCli.py
# 干啥的    :
from dataclasses import dataclass, field

import redis
import time
from redis.sentinel import Sentinel

cli = redis.Redis(host='localhost', port=6379, db=0)
cli.set("admin", 'IanLeto')


def new_redis_sentinel() -> redis.sentinel:
    return Sentinel([('localhost', 26379)])


def new_redis_client(host: str = 'localhost', port: int = 6379, db: int = 0) -> redis.Redis:
    return redis.Redis(host=host, port=port, db=db)


def new_redis_pipeline(conn: redis.Redis, trans: bool = False) -> redis.Redis.pipeline:
    return conn.pipeline(transaction=trans)


@dataclass
class RedisBackend:
    address: str
    cli: redis.Redis = new_redis_client() if 1 == 1 else new_redis_sentinel()
    port: int = 6379
    db: int = 0
    # pipeline : new_redis_pipeline
    pre: str = field(default_factory=lambda x: "aliyun" + x)
    count: int = 0


# if __name__ == '__main__':
#     r = RedisBackend(address="", cli=new_redis_client(), pre="test")
#     if r.cli.setnx("admin", "root"):
#         print("unlock")


def redis_consumer():
    while 1 == 1:
        print(cli.lpop("tList"))


def redis_producer():
    count = 0
    while 1 == 1:
        time.sleep(1)
        count += 1
        print(cli.lpush("tList", count))

    # item_list = dict(zip(list('N' * 5), range(1, 5)))


def item_watch():
    user = 'user'
    itemid = set("user", "user2")
    end = time.time() + 5
    pipe = new_redis_client().pipeline()
    while time.time() < end:
        try:
            pipe.watch(user)
            if not pipe.sismember(user, itemid):
                pipe.unwatch()
                return None
            pipe.multi()
            time.sleep(2)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass
    return False


if __name__ == '__main__':
    print(item_watch())
