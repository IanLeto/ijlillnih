# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 11:25
# @Author  : Ian Leto
# @File    : nodelist.py
# 干啥的    : LRU

from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):

        if self.cache.has_key(key):
            value = self.cache.pop()


if __name__ == '__main__':
    xx = OrderedDict()