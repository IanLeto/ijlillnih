# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 11:31 上午
# @Author  : Ian Leto
# @File    : InsertionSortList.py
# 干啥的    : 147. 对链表进行插入排序
from leetcode.baseDataStructure.nodelist import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        prev = head
        next_node = head.next
        if prev.val > next_node.val:
            pass
