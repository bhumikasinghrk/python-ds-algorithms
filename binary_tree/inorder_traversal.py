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
