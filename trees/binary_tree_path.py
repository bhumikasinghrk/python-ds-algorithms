# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def binary_tree_paths(root_node: TreeNode) -> str:
    paths = []
    if not root_node:
        return paths
    get_path(root_node, '', paths)
    return paths


def get_path(node: TreeNode, path: str, paths: [str]) -> str:
    if not node.left and not node.right:
        paths.append(path + str(node.val))
        return
    if node.left:
        get_path(node.left, path + str(node.val) + '->', paths)
    if node.right:
        get_path(node.right, path + str(node.val) + '->', paths)

