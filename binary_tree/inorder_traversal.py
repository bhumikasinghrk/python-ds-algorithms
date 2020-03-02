from typing import List
from binary_tree.tree_node import TreeNode


def inorder_traversal(root: TreeNode) -> List[int]:
    values = []
    recursive_search(root, values)
    return values


def recursive_search(root: TreeNode, values: List[int]):
    if root is not None:
        if root.left is not None:
            recursive_search(root.left, values)
        values.append(root.val)
        if root.right is not None:
            recursive_search(root.right, values)


def inorder_traversal_stack(root: TreeNode) -> List[int]:
    output = []
    stack = []
    current_node = root

    while current_node or len(stack) > 0:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left
        current_node = stack.pop()
        output.append(current_node.val)
        current_node = current_node.right

    return output
