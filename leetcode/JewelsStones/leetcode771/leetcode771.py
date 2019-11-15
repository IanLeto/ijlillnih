# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 10:54
# @Author  : Ian Leto
# @File    : leetcode771.py
# 干啥的    : 宝石与石头(leetcode 有史以来最简单的题)


def num_jewels_in_stones(J: str, S: str) -> int:
    count = 0
    for j in list(S):
        if j in list(J):
            count += 1

    return count


#
# def num_jewels_in_stones2(J: str, S: str) -> int:
#     dictJ = {}
#     dictS = {}
#     for j in list(J):
#         if not dictJ.get(j):
#             dictJ[j] = 1
#         else:
#             dictJ[j] += 1
#     for s in list(S):
#         if not dictJ.get(s):
#             dictS[s] = 1
#         else:
#             dictS[s] += 1
#     for k, v in dictJ.items():
#         if k in dictS.keys():
#


if __name__ == '__main__':
    print(num_jewels_in_stones("aA", "aAAbbbb"))
