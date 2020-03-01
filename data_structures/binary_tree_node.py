class BinaryTreeNode:

    def __init__(self, data, left_node=None, right_node=None):
        self.__data = data
        self.__left_node = left_node
        self.__right_node = right_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left_node(self):
        return self.__left_node

    @left_node.setter
    def left_node(self, node):
        self.__left_node = node

    @property
    def right_node(self):
        return self.__right_node

    @right_node.setter
    def right_node(self, node):
        self.__right_node = node
