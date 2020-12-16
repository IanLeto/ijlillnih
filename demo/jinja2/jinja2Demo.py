# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 5:07 下午
# @Author  : Ian Leto
# @File    : jinja2Demo.py
# 干啥的    : 了解jinja2 py 为了支持ucloud set

from jinja2 import PackageLoader, Environment
from jinja2 import Template

env = Environment(loader=PackageLoader)
dDict = {
    'sausage': "absolutely",
    'notebook': 'mac',
    'money': '1',
    'playstation': 'ps4'
}

# 变量替换
class Region:
    def __init__(self, region_id: str = ''):
        self.region_id = region_id

    def get_id(self):
        return self.region_id


with open('templateDemo', 'r')as f:
    buffer = f.read()
    template = Template(buffer)
    region = Region(region_id='1')
    print(template.render(dDict=dDict, region=region))
