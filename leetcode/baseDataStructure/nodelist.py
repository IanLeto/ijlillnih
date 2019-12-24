# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 11:25
# @Author  : Ian Leto
# @File    : nodelist.py
# 干啥的    : 链表
from dataclasses import dataclass


@dataclass
class LinkList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


