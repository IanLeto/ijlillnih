# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 11:03 上午
# @Author  : Ian Leto
# @File    : MergeTwoSortedLists.py
# 干啥的    : 21. 合并两个有序链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.baseDataStructure.nodelist import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l1, l2 = l2, l1
        while l1 is not None:
            if l1.val < l2.val:
                if l1.next.val < l2.next.val:
                    pass
                else:
                    temp = l2
                    l1.next = l2
                    l2.next = l1.next
                    l2 = temp
            l1 = l1.next
        return l1
