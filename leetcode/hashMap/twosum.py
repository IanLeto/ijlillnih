# -*- coding: utf-8 -*-
# @Time    : 2019/11/29 11:19
# @Author  : Ian Leto
# @File    : twosum.py
# 干啥的    : leetcode 1 两数之和


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {v: k for k, v in enumerate(nums)}
        for k, v in enumerate(nums):
            res = hashmap.get((target - v), None)
            # res != k 来判断重复数字的
            # eg {3,2,4} target =6
            # 6 -3 =3 数字不能重复利用
            if res is not None and res != k:
                return [k, res]
