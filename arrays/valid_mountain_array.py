from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    length = len(arr)
    if length <= 2:
        return False

    index = 1

    # Check increasing
    while index < length:
        if arr[index - 1] < arr[index]:
            index += 1
        else:
            break

    # Edge case: only increasing, only decreasing
    if index in [length, 1]:
        return False

    # Check decreasing
    while index < length:
        if arr[index - 1] > arr[index]:
            index += 1
        else:
            return False
    return True
