from typing import List


def max_consecutive_ones(nums: List[int]) -> int:
    max_ones, count = 0, 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            max_ones = max(max_ones, count)
            count = 0

    return max(max_ones, count)
