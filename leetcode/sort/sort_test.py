# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 1:57 下午
# @Author  : Ian Leto
# @File    : sort_test.py
# 干啥的    :
import unittest

from leetcode.sort.sort import bubble_sort


class TestSort(unittest.TestCase):

    def test_bubble_sort(self):
        ll = [1, 2, 3, 7, 2, 77, 32, 1, 1, 3, 4]
        self.assertEqual(bubble_sort(ll), sorted(ll))
