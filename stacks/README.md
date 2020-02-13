# Stacks

* [Daily Temperatures](#daily-temperatures)
* [Evaluate Reverse Polish Notation](#evaluate-reverse-polish-notation)
* [Implement Stack with Queue](#implement-stack-with-queue)
* [Min Stack](#min-stack)
* [Roman to Integer](#roman-to-integer)
* [Valid Parentheses](#valid-parentheses)

## Daily Temperatures

Leetcode

Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you
would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures:

Input: `T = [73, 74, 75, 71, 69, 72, 76, 73]`

Output: `[1, 1, 4, 2, 1, 1, 0, 0]`

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

```python
def daily_temperatures_brute_force(temps: List[int]) -> List[int]:
    daily_temps = []
    for index, temp in enumerate(temps):
        count = 0
        for sub_index in range(index + 1, len(temps)):
            count += 1
            if temps[sub_index] > temp:
                break
            if sub_index == len(temps) - 1:
                count = 0
        daily_temps.append(count)
    return daily_temps


def daily_temperatures(temps: List[int]) -> List[int]:
    daily_temps = deque()
    stack = LifoQueue()

    for index in range(len(temps) - 1, -1, -1):
        while not stack.empty() and temps[index] >= temps[stack.queue[-1]]:
            stack.get()

        if not stack.empty():
            daily_temps.appendleft(stack.queue[-1] - index)
        else:
            daily_temps.appendleft(0)
        stack.put(index)
    return list(daily_temps)
```

## Evaluate Reverse Polish Notation

Leetcode

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be
any divide by zero operation.

Example 1:

Input: `["2", "1", "+", "3", "*"]`
Output: `9`
Explanation: `((2 + 1) * 3) = 9`

Example 2:

Input: `["4", "13", "5", "/", "+"]`
Output: `6`
Explanation: `(4 + (13 / 5)) = 6`

Example 3:

Input: `["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]`
Output: `22`
Explanation: 

```text
= ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

```python
def evaluate_rpn(tokens: List[str]) -> int:
    stack = LifoQueue()

    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.put(token)
        else:
            right = int(stack.get())
            left = int(stack.get())
            stack.put(compute(left, right, token))

    return stack.get()


def compute(left: int, right: int, operator: str) -> int:
    if operator == '-':
        return left - right
    if operator == '+':
        return left + right
    if operator == '/':
        return trunc(float(left) / right)
    return left * right
```

## Implement Stack with Queue

Leetcode

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Example:

```python
stack.push(1)
stack.push(2)  
stack.top()   # returns 2
stack.pop()   # returns 2
stack.empty() # returns false
```

```python
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
```

## Min Stack

Leetcode

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

## Roman to Integer

Leetcode

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```text
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example:

Input: `"MCMXCIV"`
Output: `1994`

```python
ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_integer(roman: str) -> int:
    number = 0
    accumulator = []

    for index in range(len(roman) - 1, -1, -1):
        if accumulator and ROMAN_NUMERALS[accumulator[-1]] > ROMAN_NUMERALS[roman[index]]:
            number += ROMAN_NUMERALS[accumulator.pop()] - ROMAN_NUMERALS[roman[index]]
        else:
            accumulator.append(roman[index])
    while accumulator:
        number += ROMAN_NUMERALS[accumulator.pop()]

    return number
```

## Valid Parentheses

Leetcode

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