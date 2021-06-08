# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 8:49 下午
# @Author  : Ian Leto
# @File    : singleTest.py
# 干啥的    :

import json
import requests, pprint

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
}


def ulb4agent():
    xdata = {'product': 'ulb4', 'server_name': 'ulb4agent', 'server_version': 'ulb4-3.0.1', 'config_version': 'v0.0.72',
             'diff': 'region:1000001,az:4001'}
    payload = json.dumps(xdata)
    r = requests.post("http://localhost:8080/v1/cc/compare", data=payload, headers=headers)
    pprint.pprint(r.json())
    x = r.json()


def ulb7ulblog_agent():
    xdata = {"product": "ulb7", "server_name": "ulblog-agent", "server_version": "1.0.3",
             "config_version": "ulblog-agent-1.0.0", "diff": "region:1000001,az:4001"}

    payload = json.dumps(xdata)
    r = requests.post("http://localhost:8080/v1/cc/compare", data=payload, headers=headers)
    pprint.pprint(r.json())


def cnat2opts():
    xdata = {"product": "cnat2", "server_name": "natops", "server_version": "v0.2.2", "config_version": "v0.0.161",
             "diff": "region:1000001,az:4001"}

    payload = json.dumps(xdata)
    r = requests.post("http://localhost:8080/v1/cc/compare", data=payload, headers=headers)
    pprint.pprint(r.json())


if __name__ == '__main__':
    # ulb4agent()
    # ulb7ulblog_agent()
    cnat2opts()
