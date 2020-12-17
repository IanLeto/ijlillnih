# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 6:54 下午
# @Author  : Ian Leto
# @File    : combineConfig.py
# 干啥的    : 使用模板文件实现部署替换配置文件
from jinja2 import Environment, PackageLoader, Template
import yaml

with open('config.yml') as f:
    y = yaml.safe_load(f)

# 注意一下这里的语法
env = Environment(loader=PackageLoader('demo', 'jinja2Demo'))
template = env.get_template('nginx.j2')
content = template.render(y)

with open('config', 'w') as f:
    f.write(content)
