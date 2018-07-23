# Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval
# covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow
# the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or
# the interval is empty.
from typing import Optional


def binary_search_iterative(array: [int], target: int) -> Optional[int]:
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = int((left + right) / 2)

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        elif array[middle] > target:
            right = middle - 1
    return None


def binary_search_recursive(array: [int], left: int, right: int, target: int) -> Optional[int]:
    if right >= left:

        mid = int((left + right) / 2)

        # If element is present at the middle
        if array[mid] == target:
            return mid

        # If element is smaller than mid, then it can only be present in left subarray
        elif array[mid] > target:
            return binary_search_recursive(array, left, mid - 1, target)

        # Else the element can only be present in the right subarray
        else:
            return binary_search_recursive(array, mid + 1, right, target)
    else:
        return None