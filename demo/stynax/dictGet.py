# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 5:28 下午
# @Author  : Ian Leto
# @File    : dictGet.py
# 干啥的    : 无限遍历dict get common


def fetch_common(d: dict) -> dict:
    kv_map = {}

    def get_common_dict(val: dict):
        for k, v in val.items():
            if k == 'common':
                kv_map.update(v)
                continue
            if isinstance(v, dict):
                return get_common_dict(v)

    get_common_dict(d)
    return kv_map


if __name__ == '__main__':
    t = {
        "uver": {
            "uver-extern-scripts": {
                "common": {
                    "logPath": "/var/log/",
                    "processName": "bgpd",
                    "south": {
                        "hostIp": "{{ int_check_ip }}",
                        "assignIp": "tap_int",
                        "counter": 20,
                        "interval": 0.5,
                        "deadline": 15,
                        "lossPacket": 50
                    },
                    "north": {
                        "hostIp": "{{ ext_check_ip }}",
                        "assignIp": "tap_ext",
                        "counter": 20,
                        "interval": 0.5,
                        "deadline": 15,
                        "lossPacket": 50
                    },
                    "uuid": "{{ inventory_hostname }}",
                    "zk_server": "{{ public.region.zk }}",
                    "umonitor_access": "/NS/umonitor2/set1/access"
                }
            }
        }
    }
    import pprint

    print(fetch_common(t))
    pprint.pprint(fetch_common(t))
    s = {
        "utraffic": {
            "utrafficmanager": {
                "common": {
                    "bw": {
                        "danger_eipbw": "1",
                        "danger_sharebw": "15",
                        "default_bwin": "1000",
                        "default_bwout": "1000",
                        "default_sharebwin": "1000",
                        "default_sharebwout": "1000",
                        "outle10": "50",
                        "outle5": "50",
                        "outle50": "50"
                    },
                    "metricid": {
                        "ddos_in": 7027,
                        "ddos_out": 7028
                    },
                    "monitor": {
                        "band_in": "7002",
                        "band_out": "7003",
                        "bwshare_inbw": "7013",
                        "bwshare_inbw_buy": "7082",
                        "bwshare_inbw_percent": "7351",
                        "bwshare_outbw": "7012",
                        "bwshare_outbw_buy": "7083",
                        "bwshare_outbw_percent": "7350",
                        "eip_top_inbw": "7253",
                        "eip_top_outbw": "7252",
                        "eipid_inbw_percent": "7249",
                        "eipid_outbw_percent": "7248",
                        "eipid_top_inbw": "7255",
                        "eipid_top_outbw": "7254",
                        "exnet_packets_in": "7004",
                        "exnet_packets_out": "7005",
                        "extnet_flow_in": "7000",
                        "extnet_flow_out": "7001",
                        "in_dropped_packets_number": "7030",
                        "inbw": 7002,
                        "inbw2": "7038",
                        "inbytes": 7000,
                        "inbytes2": "7040",
                        "indropped": 7030,
                        "inpkts": 7004,
                        "interface_outbw": "7240",
                        "interface_outbytes": "7259",
                        "interface_outdropped": "7242",
                        "interface_outpkts": "7244",
                        "out_dropped_packets_number": "7029",
                        "outbw": 7003,
                        "outbw2": "7039",
                        "outbytes": 7001,
                        "outbytes2": "7041",
                        "outdropped": 7029,
                        "outpkts": 7005,
                        "sharebandwidth_in": "7082",
                        "sharebandwidth_out": "7083",
                        "tc_bandwidth_in": "7080",
                        "tc_bandwidth_out": "7081",
                        "unet_gateway_inbw": "7261",
                        "unet_gateway_inbytes": "7263",
                        "unet_gateway_indropped": "7267",
                        "unet_gateway_inpkts": "7265",
                        "unet_gateway_outbw": "7260",
                        "unet_gateway_outbytes": "7262",
                        "unet_gateway_outdropped": "7266",
                        "unet_gateway_outpkts": "7264"
                    },
                    "name": {
                        "utrafficmanager_region": "/NS/unet/set{{region_id}}/NewRegionUTrafficManager"
                    }
                },
                "ulb7": {
                    "common": {
                        "conf": {
                            "az_id": "{{az_id}}",
                            "contained_azids": "{{az_id}}",
                            "default_bw_in": 1000,
                            "default_bw_out": 1000,
                            "highrate": 110,
                            "lowrate": 100,
                            "manager_type": "az",
                            "redis_data_timeout": 3600,
                            "report": 1,
                            "reportEIP2Region": "0",
                            "reportTSDB": "1",
                            "report_bwshare": 1
                        },
                        "dbserver": {
                            "database": "unetwork"
                        },
                        "name": {
                            "manager": "/NS/unet/set{{az_id}}/ULB7UTrafficManager/master",
                            "udatabase": "/NS/region{{region_id}}/udatabase/unetwork_write_set0",
                            "utrafficmanager_az": "/NS/unet/set{{az_id}}/ULB7UTrafficManager"
                        },
                        "network": {
                            "listen_ip": "{{inventory_hostname}}",
                            "listen_port": 7212
                        },
                        "umonitor": {
                            "access": "/NS/umonitor2/set1/access"
                        }
                    },
                    "region_1000001": {
                        "az_4001": {
                            "conf": {
                                "contained_azids": "4001,5001,9001",
                                "lowrate": 110
                            },
                            "name": {
                                "udatabase": "/NS/region5001/udatabase/unetwork_set_utraffic"
                            },
                            "redis": "172.27.247.43:6379",
                            "umonitor": {
                                "access": "/NS/umonitor2/set1/access_4001"
                            }
                        },
                        "az_5001": {
                            "conf": {
                                "contained_azids": "4001,5001,9001",
                                "lowrate": 110
                            },
                            "name": {
                                "udatabase": "/NS/region5001/udatabase/unetwork_set_utraffic"
                            },
                            "redis": "10.179.64.250:6379",
                            "umonitor": {
                                "access": "/NS/umonitor2/set1/access_5001"
                            }
                        },
                        "az_9001": {
                            "conf": {
                                "contained_azids": "4001,5001,9001",
                                "lowrate": 110
                            },
                            "name": {
                                "udatabase": "/NS/region9001/udatabase/unetwork_set_utraffic"
                            },
                            "redis": "172.28.247.21:6379",
                            "umonitor": {
                                "access": "/NS/umonitor2/set1/access_9001"
                            }
                        },
                        "az_9002": {
                            "conf": {
                                "lowrate": 110
                            },
                            "redis": "172.18.180.25:6379"
                        }
                    },
                    "region_1000003": {
                        "az_7001": {
                            "name": {
                                "udatabase": "/NS/region7001/udatabase/unetwork_set0"
                            },
                            "redis": "172.27.119.2:6379",
                            "umonitor": {
                                "access": "/NS/unet/set1000003/umonitor_proxy"
                            }
                        }
                    },
                    "region_1000004": {
                        "az_3001": {
                            "name": {
                                "udatabase": "/NS/region3001/unet/udatabase/unetwork_set1"
                            },
                            "redis": "10.68.68.146:6379"
                        },
                        "az_3002": {
                            "name": {
                                "udatabase": "/NS/region3001/unet/udatabase/unetwork_set1"
                            },
                            "redis": "172.21.37.245:6379"
                        }
                    },
                    "region_1000005": {
                        "az_6001": {
                            "name": {
                                "udatabase": "/NS/region6001/udatabase/unetwork_set0"
                            },
                            "redis": "172.25.0.201:6379"
                        }
                    },
                    "region_1000009": {
                        "az_8100": {
                            "name": {
                                "udatabase": "/NS/cn-sh2/udatabase/cluster/set0/network"
                            },
                            "redis": "10.182.45.2:6379"
                        },
                        "az_8300": {
                            "name": {
                                "udatabase": "/NS/cn-sh2/udatabase/cluster/set0/network"
                            },
                            "redis": "172.20.176.143:6379"
                        }
                    },
                    "region_1000010": {
                        "az_10001": {
                            "name": {
                                "udatabase": "/NS/na02/udatabase/cluster/set0/public"
                            },
                            "redis": "172.30.2.15:6379"
                        }
                    },
                    "region_1000011": {
                        "az_10002": {
                            "name": {
                                "udatabase": "/NS/eur01/udatabase/cluster/set0/public"
                            },
                            "redis": "172.30.6.15:6379"
                        }
                    },
                    "region_1000012": {
                        "az_10003": {
                            "name": {
                                "udatabase": "/NS/sa02/udatabase/cluster/set0/public"
                            },
                            "redis": "172.30.22.15:6379"
                        },
                        "az_10026": {
                            "name": {
                                "udatabase": "/NS/sa02/udatabase/cluster/set0/public"
                            },
                            "redis": "10.65.132.169:6379"
                        }
                    },
                    "region_1000013": {
                        "az_10004": {
                            "name": {
                                "udatabase": "/NS/ea01/udatabase/cluster/set0/public"
                            },
                            "redis": "172.30.174.74:6379"
                        }
                    },
                    "region_1000014": {
                        "az_10005": {
                            "name": {
                                "udatabase": "/NS/sa01/udatabase/cluster/set0/public"
                            },
                            "redis": "172.30.14.18:6379"
                        }
                    },
                    "region_1000015": {
                        "az_10006": {
                            "name": {
                                "manager": "/NS/unet/set10006/ULB7UTrafficManager/master",
                                "udatabase": "/NS/sa03/udatabase/cluster/set0/public",
                                "utrafficmanager_az": "/NS/unet/set10006/ULB7UTrafficManager"
                            },
                            "redis": "172.30.18.15:6379"
                        }
                    },
                    "region_1000016": {
                        "az_10007": {
                            "name": {
                                "manager": "/NS/unet/set10007/ULB7UTrafficManager/master",
                                "udatabase": "/NS/region10007/udatabase/public",
                                "utrafficmanager_az": "/NS/unet/set10007/ULB7UTrafficManager"
                            },
                            "redis": "172.30.30.175:6379"
                        }
                    },
                    "region_1000017": {
                        "az_10008": {
                            "name": {
                                "udatabase": "/NS/region1000017/udatabase/unetwork"
                            },
                            "redis": "172.30.34.109:6379"
                        }
                    },
                    "region_1000018": {
                        "az_10009": {
                            "name": {
                                "udatabase": "/NS/region1000018/udatabase/unetwork"
                            },
                            "redis": "172.30.38.248:6379"
                        }
                    },
                    "region_1000019": {
                        "az_10010": {
                            "name": {
                                "udatabase": "/NS/region1000019/udatabase/unetwork"
                            },
                            "redis": "172.30.58.16:6379"
                        }
                    },
                    "region_1000020": {
                        "az_10011": {
                            "name": {
                                "udatabase": "/NS/region1000020/udatabase/unetwork"
                            },
                            "redis": "172.30.42.49:6379"
                        }
                    },
                    "region_1000021": {
                        "az_110200": {
                            "name": {
                                "udatabase": "/NS/region1000021/udatabase/unetwork"
                            },
                            "redis": "172.20.12.125:6379"
                        }
                    },
                    "region_1000022": {
                        "az_10012": {
                            "name": {
                                "udatabase": "/NS/region1000022/udatabase/unetwork"
                            },
                            "redis": "172.29.146.17:6379"
                        }
                    },
                    "region_1000023": {
                        "az_10013": {
                            "name": {
                                "udatabase": "/NS/region1000023/udatabase/unetwork"
                            },
                            "redis": "172.30.46.136:6379"
                        }
                    },
                    "region_1000037": {
                        "az_10025": {
                            "name": {
                                "udatabase": "/NS/region1000037/udatabase/unetwork"
                            },
                            "redis": "10.65.5.146:6379"
                        }
                    },
                    "region_1200200": {
                        "az_1200201": {
                            "name": {
                                "udatabase": "/NS/region1200200/udatabase/unetwork"
                            },
                            "redis": "10.64.68.246:6379"
                        }
                    },
                    "region_1000027": {
                        "az_10015": {
                            "name": {
                                "udatabase": "/NS/region1000027/udatabase/unetwork"
                            },
                            "redis": "172.30.50.148:6379"
                        }
                    },
                    "region_1000028": {
                        "az_10016": {
                            "name": {
                                "udatabase": "/NS/region1000028/udatabase/unetwork"
                            },
                            "redis": "172.30.54.184:6379"
                        }
                    },
                    "region_1000030": {
                        "az_10018": {
                            "name": {
                                "udatabase": "/NS/region1000030/udatabase/unetwork"
                            },
                            "redis": "172.24.18.170:6379"
                        }
                    },
                    "region_1000029": {
                        "az_10017": {
                            "name": {
                                "udatabase": "/NS/region1000029/udatabase/unetwork"
                            },
                            "redis": "172.30.62.194:6379"
                        }
                    },
                    "region_1000007": {
                        "az_8001": {
                            "name": {
                                "udatabase": "/NS/region8001/udatabase/unetwork_set0"
                            },
                            "redis": "172.29.15.250:6379"
                        }
                    }
                }
            }
        }
    }
    pprint.pprint(fetch_common(s))
