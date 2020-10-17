from binary_tree.tree_node import TreeNode


def generate_binary_tree() -> TreeNode:
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    return head
