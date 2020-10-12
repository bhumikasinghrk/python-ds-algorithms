from typing import List


def two_sum(array: List[int], target: int) -> List[int]:
    complements = dict()

    for index, number in enumerate(array):
        complement = target - number
        if complement in complements:
            return [complements[complement], index]
        complements[number] = index

    return [-1, -1]
