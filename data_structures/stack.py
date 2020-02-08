from typing import Generic, TypeVar

T = TypeVar('T')


class StackList(Generic[T]):
    """
    Stack backed by List. List is O(1) for append and pop
    """
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def push(self, data: T):
        self.__list.append(data)

    def pop(self) -> T:
        return self.__list.pop()
