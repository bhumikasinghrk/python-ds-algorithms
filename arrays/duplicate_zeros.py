from typing import List


def duplicate_zeros(arr: List[int]) -> List[int]:
    stack = []
    index = 0
    length = len(arr)

    while len(stack) < length:
        stack.append(arr[index])

        if len(stack) < length and arr[index] == 0:
            stack.append(0)
        index += 1

    for i in range(length - 1, -1, -1):
        arr[i] = stack.pop()

    return arr
