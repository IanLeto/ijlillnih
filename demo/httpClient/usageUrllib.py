# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 5:57 下午
# @Author  : Ian Leto
# @File    : usageUrllib.py
# 干啥的    : 如何使用python 做http

import urllib.request
import urllib.error
import socket


# 拉取网页内容
def fetch_web_page(url: str):
    return urllib.request.urlopen(url=url)


def get_request(url: str, path: str, timeout: float = 10):
    return urllib.request.urlopen(url + path, timeout=timeout)


def post_request(url: str, path: str, data: dict, timeout: float = 10):
    return urllib.request.urlopen(url + path, data=data, timeout=timeout)


if __name__ == '__main__':
    # 调用 get
    try:
        res = get_request(url="http://httpbin.org", path='/get')
        print(res.status)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("Time Out")

