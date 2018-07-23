from typing import Optional

# The most basic search. Start from the leftmost element of the array and one by one compare the target with each
# element of the array. If the target matches with an element, return the index.


def linear_search(array: [int], left: int, right: int, target: int) -> Optional[int]:
    for index in range(left, right + 1):
        if array[index] == target:
            return index
    return None
