from collections import deque
from typing import List
from binary_tree.tree_node import TreeNode


def level_order_traversal(root: TreeNode) -> List[List[int]]:
    values = []

    if not root:
        return values

    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        values.append(level)

    return values
