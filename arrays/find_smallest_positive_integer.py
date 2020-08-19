from typing import List


def find_smallest_positive_integer(arr: List[int]) -> int:
    length = len(arr)

    if length == 0:
        return 0

    smallest = None

    for i in range(length):
        if arr[i] > 0:
            if smallest is None:
                smallest = arr[i]
            elif arr[i] < smallest:
                smallest = arr[i]

    if smallest is None:
        return 0
    return smallest
