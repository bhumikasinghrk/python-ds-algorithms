from math import trunc
from typing import List
from queue import LifoQueue


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
