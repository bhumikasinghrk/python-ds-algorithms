from data_structures.binary_tree_node import BinaryTreeNode


class BinaryTree(object):
    def __init__(self, root: BinaryTreeNode = None):
        self._root = root

    @property
    def root(self) -> BinaryTreeNode:
        return self._root

    @root.setter
    def root(self, root: BinaryTreeNode):
        self._root = root
