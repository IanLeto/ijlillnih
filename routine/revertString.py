# -*- coding: utf-8 -*-
# @Time    : 2020/1/10 10:45 上午
# @Author  : Ian Leto
# @File    : revertString.py
# 干啥的    :
from leetcode.baseDataStructure.nodelist import ListNode
from leetcode.baseDataStructure.tree import TreeNode


def revert_list(node: ListNode) -> ListNode:
    res = None
    if node is None:
        return node
    while node.next is not None:
        temp = node.next
        node.next = res
        res = node
        node = temp
    return res


# 递归二叉树
def sdaf(t1: TreeNode):
    if t1 is None:
        return None
    sdaf(t1.left)


if __name__ == '__main__':
    class x:
        def __init__(self):
            pass

        def __set__(self, instance, value):
            pass

        def __str__(self):
            return 11


    ss = x()
    print(ss.__hash__())
    print(hash(ss.__hash__()))
