# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 11:37 上午
# @Author  : Ian Leto
# @File    : routineStack.py
# 干啥的    :
from time import time


def IanTimeCalc(func):
    start = time()
    result = func()
    stop = time()
    run_time = str(stop - start)

    return run_time


class Solution:
    @IanTimeCalc
    def isValid(self, s: str) -> bool:
        list1 = ['(', '{', '[']
        list2 = [')', ']', '}']
        list3 = ['()', '[]', '{}']
        l = []

        for i in s:
            if i in list1:
                l.append(i)
            if i in list2:
                ss = i + l[-1]
                if ss in list3:
                    print(l.pop())
                    continue
                else:
                    return False
        if len(l) != 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
