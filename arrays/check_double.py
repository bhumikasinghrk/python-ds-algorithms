from typing import List


def check_double(arr: List[int]) -> bool:
    elements = set()

    for num in arr:
        if num * 2 in elements:
            return True
        if num % 2 == 0 and num / 2 in elements:
            return True
        elements.add(num)

    return False
