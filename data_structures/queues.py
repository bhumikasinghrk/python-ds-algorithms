from typing import Generic, TypeVar, List
from data_structures.doublylinkedlist import DoublyLinkedList

T = TypeVar('T')


class QueueList(Generic[T]):
    """
    Basic queue backed with a list. Not optimal since list has O(N) complexity for
    inserting and removing elements at the beginning
    """

    def __init__(self):
        self.queue: List[T] = []

    def __len__(self):
        return len(self.queue)

    def dequeue(self) -> T:
        return self.queue.pop(0)

    def enqueue(self, element: T):
        self.queue.append(element)


class QueueLinkList(Generic[T]):
    """
    Queue backed by a doubly linked list
    """

    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def __len__(self):
        return self.linked_list.size()

    # O(1)
    def dequeue(self) -> T:
        return self.linked_list.remove(0)

    # O(1)
    def enqueue(self, element: T):
        self.linked_list.append(element)
