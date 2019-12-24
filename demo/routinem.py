from leetcode.baseDataStructure.nodelist import LinkList
from leetcode.baseDataStructure.tree import TreeNode, create


def aaa(root_node: TreeNode):
    link = []

    def res(node: TreeNode):
        if node is None:
            return node
        else:
            link.append(node.val)
            res(node.left)
            res(node.right)

    res(root_node)
    return link


def BsfR(root_node: TreeNode):
    pass


if __name__ == '__main__':
    root = create(TreeNode(0))
    print(aaa(root))
