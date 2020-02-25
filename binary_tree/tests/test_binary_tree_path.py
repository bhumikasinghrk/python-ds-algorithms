from binary_tree.binary_tree_path import TreeNode, binary_tree_paths


def test_binary_tree_paths():
    root_node = TreeNode(1)
    root_node.left = TreeNode(2)
    root_node.right = TreeNode(3)
    root_node.left.left = TreeNode(5)
    assert binary_tree_paths(root_node) == ["1->2->5", "1->3"]
