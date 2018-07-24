class BinaryTreeNode:

    def __init__(self, data, left_node=None, right_node=None):
        self._data = data
        self._left_node = left_node
        self._right_node = right_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left_node(self):
        return self._left_node

    @left_node.setter
    def left_node(self, node):
        self._left_node = node

    @property
    def right_node(self):
        return self._right_node

    @right_node.setter
    def right_node(self, node):
        self._right_node = node