from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree_node import BinaryTreeNode


def test_init():
    tree = BinaryTree()
    assert not tree.root

    root = BinaryTreeNode(1)
    tree = BinaryTree(root)
    assert tree.root.data == 1


def test_root():
    tree = BinaryTree()
    root = BinaryTreeNode(1)
    tree.root = root
    assert tree.root == root