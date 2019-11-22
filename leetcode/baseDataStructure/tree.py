# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 10:40
# @Author  : Ian Leto
# @File    : tree.py
# 干啥的    : 二叉树基本数据结构
import os


class TreeNode:
    def __call__(self, *args, **kwargs):
        return self.__str__()

    def __str__(self):
        return dict(zip({'path'}, {os.getcwd()}))

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, node_value):
        self.left = TreeNode(node_value)
        return self.left

    def insert_right(self, node_value):
        self.right = TreeNode(node_value)
        return self.right


def create(root_node):
    A = root_node.insert_left('A')
    C = A.insert_left('C')
    D = A.insert_right('D')
    F = D.insert_left('F')
    G = D.insert_right('G')
    B = root_node.insert_right('B')
    E = B.insert_right('E')
    return root_node


# 前序遍历 -- 递归
def pre_order_traverse_recursive(root: TreeNode):
    if not root:
        return None
    print(root.val)
    pre_order_traverse_recursive(root.left)
    pre_order_traverse_recursive(root.right)


def middle_order_traverse_recursive(root: TreeNode) -> TreeNode:
    if not root:
        return None


# tree 转 链表
def pre_order_traverse_recursive_to_node_list(root_node: TreeNode) -> list:
    result = []

    def solution(root: TreeNode):
        if not root:
            return
        result.append(root)
        solution(root.left)
        solution(root.right)

    solution(root_node)
    return result


if __name__ == '__main__':
    root = TreeNode('root')
    print(root())
    root = create(root)
    pre_order_traverse_recursive(root)
    print([i.val for i in pre_order_traverse_recursive_to_node_list(root)])
