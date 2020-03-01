from typing import List
from binary_tree.tree_node import TreeNode

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def preorder_traversal_iterative(root: TreeNode) -> List[int]:
    output = []

    if root is None:
        return output

    stack = [root]
    while stack:
        root_node = stack.pop()
        if root_node is not None:
            output.append(root_node.val)
        if root_node.right is not None:
            stack.append(root_node.right)
        if root_node.left is not None:
            stack.append(root_node.left)
    return output
