# -*- coding: utf-8 -*-
# @Time    : 2019/11/12 11:30
# @Author  : Ian Leto
# @File    : FlattenBinaryTreetoLinkedList.py
# 干啥的    : 二叉树展开为链表
from leetcode.baseDataStructure import tree


def flatten(root: tree.TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    def hepler(root):
        if root is None:
            return
        help(root.left)
        help(root.right)
        if root.left is not None:
            pre = root.left
            while pre.right:  # 找到左子树的最右节点
                pre = pre.right

