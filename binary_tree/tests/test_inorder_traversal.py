from binary_tree.binary_tree_generator import generate_binary_tree
from binary_tree.inorder_traversal import inorder_traversal, inorder_traversal_stack


def test_inorder_traversal():
    tree = generate_binary_tree()
    assert inorder_traversal(tree) == [4, 2, 5, 1, 3]


def test_inorder_traversal_stack():
    tree = generate_binary_tree()
    assert inorder_traversal_stack(tree) == [4, 2, 5, 1, 3]
