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


def preorder_traversal_morris(root: TreeNode) -> List[int]:
    node, output = root, []
    while node:
        if not node.left:
            output.append(node.val)
            node = node.right
        else:
            predecessor = node.left

            while predecessor.right and predecessor.right is not node:
                predecessor = predecessor.right

            if not predecessor.right:
                output.append(node.val)
                predecessor.right = node
                node = node.left
            else:
                predecessor.right = None
                node = node.right

    return output


def preorder_traversal_recursive(root: TreeNode) -> List[int]:
    values = []
    if not root:
        return values

    values.append(root.val)

    if root.left:
        values.extend(preorder_traversal_recursive(root.left))
    if root.right:
        values.extend(preorder_traversal_recursive(root.right))
    return values
