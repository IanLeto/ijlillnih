import time

import redis

pipe = redis.Redis().pipeline(transaction=True)
cli = redis.Redis()


def list_item(conn, item_id, seller_id, price):
    pipe.watch(u'localhost:1222')
    if not pipe.sismember(item_id, 'kk'):
        pipe.unwatch()
        return None

    pipe.multi()
    # do something
    pipe.execute()


def lock_item(key: str):
    cli.setnx()
    cli.setex()


def trans():
    cli.incr('trans1')
    time.sleep(.1)


