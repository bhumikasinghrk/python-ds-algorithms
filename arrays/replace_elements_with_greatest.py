from typing import List


def replace_elements_with_greatest(arr: List[int]) -> List[int]:
    length = len(arr)
    max_number = -1

    for index in range(length - 1, -1, -1):
        temp = arr[index]
        arr[index] = max_number
        max_number = max(temp, max_number)

    return arr
