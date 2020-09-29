# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 5:12 下午
# @Author  : Ian Leto
# @File    : usageDemo.py
# 干啥的    : 举例如何使用

from demo.httpClient import httpClient

if __name__ == '__main__':
    cli = httpClient.HttpClient("httpbin.org")
    print(str(cli.get_request("/get").read()))

