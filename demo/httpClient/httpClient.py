# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 5:00 下午
# @Author  : Ian Leto
# @File    : httpClient.py
# 干啥的    : python 版本的httpclient

import http.client
import urllib.request
import urllib.parse


def get_request_with_params(path: str, safe: str = ':/?=&'):
    url = urllib.parse.quote(path, safe)
    return urllib.request.urlopen(url)


class HttpClient:

    def __init__(self, url: str):
        self.conn = url
        self.Client = http.client.HTTPConnection(self.conn)

    def _get_client(self):
        return self.Client

    def _ping(self):
        pass

    def _get_request(self, path: str):
        self.Client.request("GET", path)
        res = self.Client.getresponse()
        return res

    def get_request(self, path: str):
        self.Client.request("GET", path)
        return self.Client.getresponse()

    def post_request(self, path: str, body: dict):
        pass

