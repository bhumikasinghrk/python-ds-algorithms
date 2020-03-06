from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T = None, previous_node: 'Node' = None, next_node: 'Node' = None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node


# Wikipedia: In a 'doubly linked list', each node contains, besides the next-node link, a second link field pointing
# to the 'previous' node in the sequence. The two links may be called 'forward('s') and 'backwards', or 'next' and
# 'prev'('previous').


class DoublyLinkedList(Generic[T]):

    def __init__(self):
        self.__head = Node()
        self.__tail = Node()

        self.__head.next_node = self.__tail
        self.__tail.previous_node = self.__head

    # O(N)
    def all_values(self) -> [T]:
        values = []
        node = self.__head.next_node

        while node is not self.__tail:
            values.append(node.data)
            node = node.next_node

        return values

    # O(1)
    def append(self, data: T):
        # Last <-> Tail --> Last <-> New <-> Tail
        node = Node(data)
        last_node = self.__tail.previous_node

        last_node.next_node = node
        node.previous_node = last_node

        node.next_node = self.__tail
        self.__tail.previous_node = node

    # O(N)
    def get_node(self, index: int) -> Optional[Node]:
        current_node = self.__head.next_node
        count = 0

        while current_node is not self.__tail:
            if count == index:
                return current_node
            current_node = current_node.next_node
            count += 1
        return None

    # O(N)
    def get(self, index: int) -> Optional[T]:
        node = self.get_node(index)
        if node:
            return node.data
        return None

    # O(N)
    def insert(self, data: T, index: int):
        node = Node(data)
        current_node: Node = self.get_node(index)

        if not current_node and index == 0:
            self.__head.next_node = node
            node.previous_node = self.__head
            node.next_node = self.__tail
            self.__tail.previous_node = node
            return

        if not current_node:
            raise IndexError("Index out of bounds")

        # Previous <-> Original --> Previous <-> New <-> Original
        current_node.previous_node.next_node = node
        node.previous_node = current_node.previous_node
        node.next_node = current_node
        current_node.previous_node = node

    # O(N)
    def remove(self, index: int) -> Optional[T]:
        node = self.get_node(index)
        if not node:
            return None

        # Previous <-> Node <-> Next --> Previous <-> Next
        node.previous_node.next_node = node.next_node
        node.next_node.previous_node = node.previous_node

        return node.data

    # O(N)
    def size(self) -> int:
        count = 0
        node = self.__head.next_node

        while node != self.__tail:
            count += 1
            node = node.next_node
        return count
