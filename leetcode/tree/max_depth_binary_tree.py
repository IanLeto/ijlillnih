# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 11:46
# @Author  : Ian Leto
# @File    : reversal_tree.py
# 干啥的    : 104. Maximum Depth of Binary Tree 二叉树最大深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.baseDataStructure.tree import TreeNode

'''
    难点在于如何处理递归中计数问题
'''


class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        def res(node: TreeNode) -> int:
            if node is None:
                return 0
            else:
                left_height = res(node.left)
                right_height = res(node.right)
                # '''
                #     这里注意递归函数的处理思想
                #     取递归中间状态 即
                #     1。我已将拿到了left 和 right 的深度
                #     2。这一层的深度为 left + right 的适深度 + 1
                #
                # '''
                return max(left_height, right_height) + 1

        return res(root)
