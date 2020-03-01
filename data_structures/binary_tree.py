from data_structures.binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: BinaryTreeNode = None):
        self.__root = root

    @property
    def root(self) -> BinaryTreeNode:
        return self.__root

    @root.setter
    def root(self, root: BinaryTreeNode):
        self.__root = root
