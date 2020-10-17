from typing import List
from binary_tree.tree_node import TreeNode


def postorder_traversal_recursive(root: TreeNode) -> List[int]:
    values = []
    if not root:
        return values

    if root.left:
        values.extend(postorder_traversal_recursive(root.left))
    if root.right:
        values.extend(postorder_traversal_recursive(root.right))

    values.append(root.val)

    return values


def postorder_traversal_iterative(root: TreeNode) -> List[int]:
    values = []
    stack = []

    while root or stack:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()

        if stack and root.right == stack[-1]:
            stack[-1] = root
            root = root.right
        else:
            values.append(root.val)
            root = None

    return values
