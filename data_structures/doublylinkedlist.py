from typing import Optional


class Node:
    def __init__(self, data=None, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node


# Wikipedia: In a 'doubly linked list', each node contains, besides the next-node link, a second link field pointing
# to the 'previous' node in the sequence. The two links may be called 'forward('s') and 'backwards', or 'next' and
# 'prev'('previous').


class DoublyLinkedList(object):

    def __init__(self) -> None:
        self._head = Node()
        self._tail = Node()

        self._head.next_node = self._tail
        self._tail.previous_node = self._head

    # O(N)
    def all_values(self) -> [int]:
        values = []
        node = self._head.next_node

        while node and node.next_node:
            values.append(node.data)
            node = node.next_node

        return values

    # O(1)
    def append(self, node: Node) -> None:
        last_node = self._tail.previous_node
        # Last <-> Tail --> Last <-> New <-> Tail

        # Link the new node to the original last node and the tail
        last_node.next_node = node
        node.previous_node = last_node

        # Point the tail to the new last node
        node.next_node = self._tail
        self._tail.previous_node = node

    # O(N)
    def get_node(self, index: int) -> Optional[Node]:
        current_node = self._head.next_node
        if current_node == self._tail:  # empty list
            return None

        count = 0

        while current_node:
            if count == index:
                return current_node
            current_node = current_node.next_node
            count += 1
        return None

    # O(N)
    def get_value(self, index: int) -> Optional[int]:
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def insert(self, node: Node, index: int) -> None:
        original_node = self._tail

        if index != 0 or self._head.next_node != self._tail:  # empty list
            original_node = self.get_node(index)

        if not original_node:
            raise IndexError("Node not present at index")

        previous_node = original_node.previous_node
        # Previous <-> Original --> Previous <-> New <-> Original
        previous_node.next_node = node  # previous node points to the new node
        node.previous_node = previous_node  # previous node is new node's previous node
        node.next_node = original_node  # new node's next node is the original node
        original_node.previous = node  # original node's previous node is the new node

    # O(N)
    def remove(self, index: int) -> Optional[int]:
        node = self.get_node(index)
        if not node:
            return None  # Could also raise an exception

        previous_node = node.previous_node
        next_node = node.next_node

        # Previous <-> Node <-> Next --> Previous <-> Next
        previous_node.next_node = next_node
        next_node.previous_node = previous_node

        return node.data

    # O(N)
    def size(self) -> int:
        count = 0
        node = self._head.next_node

        while node != self._tail:
            count += 1
            node = node.next_node
        return count
