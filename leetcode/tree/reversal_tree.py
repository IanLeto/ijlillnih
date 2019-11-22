# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 11:46
# @Author  : Ian Leto
# @File    : reversal_tree.py
# 干啥的    : 翻转二叉树 leetcode 226
from leetcode.baseDataStructure.tree import TreeNode


def reversal_tree(root: TreeNode):
    def solve(root_node: TreeNode):
        if not root_node:
            return
        root_node.right, root_node.left = root_node.left, root_node.right
        solve(root_node=root_node.left)
        solve(root_node=root_node.right)

    solve(root)
    return root
