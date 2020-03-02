from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T = None, next_node: 'Node' = None):
        self.data = data
        self.next_node = next_node


# Wikipedia: Singly linked lists contain nodes which have a data field as well as 'next' field, which points to the next
# node in line of nodes. Operations that can be performed on singly linked lists include insertion, deletion and
# traversal.


class SinglyLinkedList(Generic[T]):

    def __init__(self):
        self.__head = Node()

    def all_values(self) -> [T]:
        values = []
        node = self.__head.next_node

        while node:
            values.append(node.data)
            node = node.next_node

        return values

    # O(N)
    def append(self, data: T) -> None:
        node = Node(data)
        last_node = self.__head

        while last_node:
            if not last_node.next_node:
                break
            last_node = last_node.next_node
        last_node.next_node = node

    # O(N)
    def get(self, index: int) -> Optional[T]:
        current_node = self.__head.next_node
        count = 0

        while current_node:
            if count == index:
                break
            current_node = current_node.next_node
            count += 1
        if current_node is None or count != index:
            return None
        return current_node.data

    def insert(self, data: T, index: int) -> None:
        node = Node(data)
        current_node = self.__head
        count = 0
        while current_node:
            if count == index:
                next_node = current_node.next_node
                node.next_node = next_node
                current_node.next_node = node
                return
            current_node = current_node.next_node
            count += 1
        if count < index:
            IndexError('Index out of bounds')

    def remove(self, index: int) -> None:
        count = 0
        current_node = self.__head

        while current_node:
            if count == index:
                remove_node = current_node.next_node
                if remove_node and remove_node.next_node:
                    current_node.next_node = remove_node.next_node
                    return
                current_node.next_node = None
            current_node = current_node.next_node
            count += 1

    # O(N)
    def size(self) -> int:
        count = 0
        current_node = self.__head.next_node

        while current_node:
            count += 1
            current_node = current_node.next_node
        return count
