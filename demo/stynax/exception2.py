# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 3:50 下午
# @Author  : Ian Leto
# @File    : exception2.py
# 干啥的    :


def get_list(l: list):
    try:
        return [i for i in l][0]
    except (ValueError, IndexError):
        return []
    except Exception as e:
        # raise
        raise


class mkc_api_error:
    def __init__(self, err, msg):
        self.err = err
        # self.msg = getattr(error_codes, err)


if __name__ == '__main__':
    print(get_list(0))


class MKCExecption(Exception):
    pass