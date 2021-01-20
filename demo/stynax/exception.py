# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 3:18 下午
# @Author  : Ian Leto
# @File    : exception.py
# 干啥的    : python 异常处理

'''

基本语法
    try:
    可能产生异常的代码块
except [ (Error1, Error2, ... ) [as e] ]:
    处理异常的代码块1
except [ (Error3, Error4, ... ) [as e] ]:
    处理异常的代码块2
except  [Exception]:
    处理其它异常
'''


def get_list(l: list):
    return [i for i in l][0]


if __name__ == '__main__':
    # 处理异常的语法
    a = 0
    try:
        a = get_list((1))
    except (TypeError, IndexError) as e:
        print('the correct input is necessary: {0}'.format(e))
    except Exception as e:
        print('unknown exception: {0}'.format(e))
    else:
        print('卧槽 全输对了？')
    finally:
        print('我一定会最后执行')
        if not a:
            raise ValueError('最终执行有误')
    print(a)
    print(1)

