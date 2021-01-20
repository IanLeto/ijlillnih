# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 5:41 下午
# @Author  : Ian Leto
# @File    : renderTemplate.py
# 干啥的    :

from jinja2 import Environment, PackageLoader, Template
from jinja2 import exceptions

if __name__ == '__main__':
    t = Template(
        "#!/usr/bin/python#ConfiglogPath='{{logPath}}'processName='{{processName}}'ipArray=[{'hostIp':'{{south.hostIp}}',#South'assignIp':'{{south.assignIp}}','counter':{{south.counter}},'interval':{{south.interval}},'deadline':{{south.deadline}},'lossPacket':{{south.lossPacket}}},{'hostIp':'{{north.hostIp}}',#North'assignIp':'{{north.assignIp}}','counter':{{north.counter}},'interval':{{north.interval}},'deadline':{{north.deadline}},'lossPacket':{{north.lossPacket}}}]uuid='{{uuid}}'zk_server='{{public.region.zk}}'umonitor_access='{{umonitor_access}}'")
    # t.render({'uver': {'uver-extern-scripts': {'common': {'logPath': '/var/log/', 'processName': 'bgpd',
    #                                                       'south': {'hostIp': '{{ int_check_ip }}',
    #                                                                 'assignIp': 'tap_int', 'counter': 20,
    #                                                                 'interval': 0.5, 'deadline': 15, 'lossPacket': 50},
    #                                                       'north': {'hostIp': '{{ ext_check_ip }}',
    #                                                                 'assignIp': 'tap_ext', 'counter': 20,
    #                                                                 'interval': 0.5, 'deadline': 15, 'lossPacket': 50},
    #                                                       'uuid': '{{ inventory_hostname }}',
    #                                                       'zk_server': '{{ public.region.zk }}',
    #                                                       'umonitor_access': '/NS/umonitor2/set1/access'}}},
    #           'logPath1': 'value1'})
    v = {'uver': {'uver-extern-scripts': {'common': {'logPath': '/var/log/', 'processName': 'bgpd',
                                                     'south': {'hostIp': '{{ int_check_ip }}',
                                                               'assignIp': 'tap_int', 'counter': 20,
                                                               'interval': 0.5, 'deadline': 15, 'lossPacket': 50},
                                                     'north': {'hostIp': '{{ ext_check_ip }}',
                                                               'assignIp': 'tap_ext', 'counter': 20,
                                                               'interval': 0.5, 'deadline': 15, 'lossPacket': 50},
                                                     'uuid': '{{ inventory_hostname }}',
                                                     'zk_server': '{{ public.region.zk }}',
                                                     'umonitor_access': '/NS/umonitor2/set1/access'}}},
         'logPath1': 'value1'}

    def ref(v: dict):

        x = v.items()
        for k,value in v.items():

        nex = False
        if isinstance(x,dict):
            nex = True
        try:
            t.render(x)
        except Exception as e:
            if isinstance(e, exceptions.UndefinedError) and nex:
                raise Exception(e)
        return ref(x)
    ref(v)
