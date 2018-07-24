from data_structures.binary_tree_node import BinaryTreeNode


def test_init():
    tree = BinaryTreeNode(1)
    left_node = BinaryTreeNode(2)
    right_node = BinaryTreeNode(3)

    assert tree.data == 1
    assert not tree.left_node
    assert not tree.right_node

    tree = BinaryTreeNode(1, left_node, right_node)
    assert tree.left_node.data == 2
    assert tree.right_node.data == 3


def test_left_node():
    left_node = BinaryTreeNode(2)
    tree = BinaryTreeNode(1)
    tree.left_node = left_node
    assert tree.left_node.data == 2


def test_right_node():
    right_node = BinaryTreeNode(2)
    tree = BinaryTreeNode(1)
    tree.right_node = right_node
    assert tree.right_node.data == 2