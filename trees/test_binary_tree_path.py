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


def binaryTreePaths(root):
    paths = []
    if not root:
        return paths
    getPath(root, '', paths)
    return paths


def getPath(node, path, paths):
    if not node.left and not node.right:
        paths.append(path + str(node.val))
    if node.left:
        getPath(node.left, path + str(node.val) + '->', paths)
    if node.right:
        getPath(node.right, path + str(node.val) + '->', paths)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)

def test_binaryTreePaths():
    assert binaryTreePaths(root) == ["1->2->5", "1->3"]


print(binaryTreePaths(root))
