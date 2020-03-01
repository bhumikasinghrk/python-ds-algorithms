from binary_tree.tree_node import TreeNode


def generate_binary_tree() -> TreeNode:
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(5)
    head.left.left = TreeNode(3)
    head.left.right = TreeNode(4)
    return head
