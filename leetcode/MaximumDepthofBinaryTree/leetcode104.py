# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 10:39
# @Author  : Ian Leto
# @File    : leetcode104.py
# 干啥的    : 二叉树的最大深度

from leetcode.baseDataStructure import tree


def max_depth(root: tree.TreeNode) -> int:
    if root is None:
        return 0
    else:
        r = max_depth(root.right)
        l = max_depth(root.left)
        num = max(r, l)


if __name__ == '__main__':
    pass
