from typing import Deque, Generic, TypeVar
from collections import deque

T = TypeVar('T')


class Stack(Generic[T]):

    def __init__(self):
        self.stack: Deque[T] = deque()

    def push(self, item: T) -> None:
        self.stack.append(item)

    def pop(self) -> T:
        return self.stack.pop()

    def top(self) -> T:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
