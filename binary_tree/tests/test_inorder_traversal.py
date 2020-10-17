from binary_tree.binary_tree_generator import generate_binary_tree
from binary_tree.inorder_traversal import inorder_traversal, inorder_traversal_stack


def test_inorder_traversal():
    tree = generate_binary_tree()
    assert inorder_traversal(tree) == [3, 2, 4, 1, 5]


def test_inorder_traversal_stack():
    tree = generate_binary_tree()
    assert inorder_traversal_stack(tree) == [3, 2, 4, 1, 5]
