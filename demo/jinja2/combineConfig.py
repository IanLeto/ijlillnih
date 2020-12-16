# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 6:54 下午
# @Author  : Ian Leto
# @File    : combineConfig.py
# 干啥的    : 使用模板文件实现部署替换配置文件
from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('jinja2'))
