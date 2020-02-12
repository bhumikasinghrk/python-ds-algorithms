from typing import Generic, TypeVar
from collections import deque

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self.queue = deque()

    def push(self, item: T) -> None:
        self.queue.append(item)

    def pop(self) -> T:
        return self.queue.popleft()

    def peek(self) -> T:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
