from binary_tree.binary_tree_generator import generate_binary_tree
from binary_tree.level_order_traversal import level_order_traversal


def test_level_order_traversal():
    tree = generate_binary_tree()
    assert level_order_traversal(tree) == [[1], [2, 3], [4, 5]]
