from _collections import deque


class MinStack:
    def __init__(self):
        self.stack = deque()
        self.min_index = 0

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.stack[self.min_index] > value:
            self.min_index = len(self.stack) - 1

    def pop(self) -> None:
        if self.min_index == len(self.stack) - 1:
            self.stack.pop()
            self.min_index = 0
            for index, value in enumerate(self.stack):
                if value < self.stack[self.min_index]:
                    self.min_index = index
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def get_min(self) -> int:
        return self.stack[self.min_index]
