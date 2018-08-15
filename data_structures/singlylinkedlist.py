from typing import Optional


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

# Wikipedia: Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next
# node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and
# traversal.


class SinglyLinkedList(object):

    def __init__(self, head: Node = None) -> None:
        self._head = head

    def all_values(self) -> []:
        values = []
        node = self._head

        while node:
            values.append(node.data)
            node = node.next_node

        return values

    # O(N)
    def append(self, node: Node) -> None:
        if not self._head:
            self._head = node
            return
        last_node = self._head

        while last_node:
            next_node = last_node.next_node
            if not next_node:
                break
            last_node = next_node
        last_node.next_node = node

    # O(N)
    def get(self, index: int) -> Optional[int]:
        if not self._head:  # No index and head is null
            return None
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def get_node(self, index: int) -> Optional[Node]:
        if not self._head:  # No index and head is null
            return None
        count = 0
        current_node = self._head

        while current_node:
            if count == index:
                return current_node
            current_node = current_node.next_node
            count += 1
        return None

    # O(N)
    def insert(self, node: Node, index: int) -> None:
        # None --> Node
        if not self._head:
            self._head = node
        # Head -> .... --> Node -> Head -> ....
        elif index == 0:
            node.next_node = self._head
            self._head = node
        # Previous -> Next --> Previous -> Node -> Next
        else:
            previous_node = self.get_node(index - 1)
            if not previous_node:
                raise IndexError("Index out of bounds")
            node.next_node = previous_node.next_node
            previous_node.next_node = node

    # O(N)
    def remove(self, index: int) -> Optional[int]:
        value = None

        if index == 0 and self._head:
            value = self._head.data
            self._head = self._head.next_node
        else:
            previous_node = self.get_node(index - 1)
            if previous_node and previous_node.next_node:
                value = previous_node.next_node.data
                previous_node.next_node = previous_node.next_node.next_node
        return value

    # O(N)
    def size(self) -> int:
        count = 0
        node = self._head

        while node:
            count += 1
            node = node.next_node
        return count