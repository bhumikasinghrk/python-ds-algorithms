from typing import Generic, TypeVar, List

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
