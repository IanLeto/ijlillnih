# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 10:40
# @Author  : Ian Leto
# @File    : tree.py
# 干啥的    : 二叉树基本数据结构


class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, node_value):
        self.left = TreeNode(node_value)
        return self.left

    def insert_right(self, node_value):
        self.right = TreeNode(node_value)
        return self.right

    def create(self, root_node):
        A = root_node.insert_left('A')
        C = A.insert_left('C')
        D = A.insert_right('D')
        F = D.insert_left('F')
        G = D.insert_right('G')
        B = root_node.insert_right('B')
        E = B.insert_right('E')
        return root_node


def pre_order_traverse(root: TreeNode):
    if not root:
        return None
    print(root.val)
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)


if __name__ == '__main__':
    root = TreeNode('root')
    root = root.create(root)
    print(root)
    pre_order_traverse(root)
