# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 5:07 下午
# @Author  : Ian Leto
# @File    : jinja2Demo.py
# 干啥的    : 了解jinja2 py 为了支持ucloud set

from jinja2 import PackageLoader, Environment
from jinja2 import Template

env = Environment(loader=PackageLoader)
dDict = {
    "syn_info": [
        {
            "cluster_id": 2105,
            "syn_addr": [
                {"addr": "172.21.48.25:12345"},
                {"addr": "172.21.48.28:12345"},
                {"addr": "10.68.80.138:12345"},
                {"addr": "10.68.80.139:12345"}
            ]
        }
    ]
}


# with open('templateDemo', 'r')as f:
#     buffer = f.read()
#     template = Template(buffer)
#     print(template.render(dDict))


def parse_config_with_business_template(config: str, business_data: dict):
    template = Template(config)

    result = template.render(business_data)
    return result


if __name__ == '__main__':
    ss = parse_config_with_business_template(
        # config='{\"syn_info\":[{\"cluster_id\":{{cluster_id}},\"syn_addr\":[{%-for listen_ip in listen_ip_list%}{\"addr\":\"{{listen_ip}}:{{udp_port}}\"}{%if not loop.last%},{%endif%}{%-endfor%}]}]}',

        # 配置文件
        config='{"db": {{主库 or 从库 }}}',
        # 数据源
        business_data=
        {
            "主库": 'ucloud:ucloud.cn0@tcp(172.30.30.163:3206)/unetwork?charset=utf8',
            "从库": 'ucloud:ucloud.cn0@tcp(172.30.30.118:3206)/unetwork?charset=utf8',
        }

    )
    print(ss)
