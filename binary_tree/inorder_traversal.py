from typing import List
from binary_tree.tree_node import TreeNode


def inorder_traversal(root: TreeNode) -> List[int]:
    values = []

    if not root:
        return values

    if root.left:
        values.extend(inorder_traversal(root.left))
    values.append(root.val)

    if root.right:
        values.extend(inorder_traversal(root.right))

    return values


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
