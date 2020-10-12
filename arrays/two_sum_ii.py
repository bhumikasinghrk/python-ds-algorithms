from typing import List


def two_sum_ii(numbers: List[int], target: int) -> List[int]:
    index_left = 0
    index_right = len(numbers) - 1

    while index_left < index_right:
        total = numbers[index_left] + numbers[index_right]
        if total < target:
            index_left += 1
        elif total > target:
            index_right -= 1
        else:
            return [index_left + 1, index_right + 1]
