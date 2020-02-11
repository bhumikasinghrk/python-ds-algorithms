# Stacks

* [Min Stack](#min-stack)
* [Valid Parentheses](#valid-parentheses)

## Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

```python
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
```

## Valid Parentheses

Given a string containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example:

```text
Input: "()[]{}"
Output: true

Input: "(]"
Output: false
```

```python
def valid_parentheses(value: str) -> bool:
    if len(value) % 2 != 0:
        return False

    closing_values = {'(': ')', '{': '}', '[': ']'}
    open_chars = closing_values.keys()
    stack = LifoQueue(len(value))

    for char in value:
        if char in open_chars:
            stack.put(char)
        else:
            if stack.empty():
                return False
            if closing_values[stack.get()] != char:
                return False

    return stack.empty()
```