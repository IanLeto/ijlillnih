# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 10:57
# @Author  : Ian Leto
# @File    : 1108.py
# 干啥的    : leetcode 1108


def defangIPAddr(address: str) -> str:
    return "".join(['[' + i + ']' for i in list(address) if i == '.'])


if __name__ == '__main__':
    print(defangIPAddr("1.1.1.1"))
