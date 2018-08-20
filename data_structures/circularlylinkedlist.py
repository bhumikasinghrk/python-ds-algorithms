from data_structures.singlylinkedlist import Node


class CircularlyLinkedList(object):
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next_node = self._head

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, node: Node):
        self._head = node
        if node:
            node.next_node = self._head

    def all_values(self) -> []:
        values = []
        node = self.head

        while node:
            values.append(node.data)
            node = node.next_node
            if node == self.head:
                break
        return values

    def append(self, node: Node):
        previous_node = self.head

        if not previous_node:
            self.head = node
            node.next_node = self.head
            return

        while previous_node.next_node != self.head:
            previous_node = previous_node.next_node

        next_node = previous_node.next_node
        previous_node.next_node = node
        node.next_node = next_node

    def remove(self, index: int):
        previous_node = self.head

        if not previous_node:
            raise IndexError("List is empty")

        if previous_node.next_node == self.head:
            self.head = None
            return

        if index == 0:
            previous_node.next_node = self.head.next_node
            self.head = previous_node.next_node
            return

        list_index = 1
        while previous_node.next_node is not self.head and list_index < index:
            previous_node = previous_node.next_node
            list_index += 1

        if list_index == index:
            next_node = previous_node.next_node
            previous_node.next_node = next_node.next_node
        else:
            raise IndexError

    def size(self) -> int:
        count = 0
        if not self.head:
            return count

        count += 1
        node = self.head.next_node

        while node and node != self.head:
            count += 1
            node = node.next_node
        return count


