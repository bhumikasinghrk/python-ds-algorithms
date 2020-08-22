from typing import List


def count_elements(arr: List[int]) -> int:
    elements = set()
    counter = 0

    for element in arr:
        elements.add(element)

    for element in arr:
        if element + 1 in elements:
            counter += 1

    return counter
