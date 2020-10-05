from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    zero = -1
    ones = 0
    highest = 0

    for index, num in enumerate(nums):
        if num == 1:
            ones += 1
        elif zero != -1:
            total = ones + 1
            if total > highest:
                highest = total
            ones = index - zero - 1
            zero = index
        else:
            zero = index

    last_total = ones

    if zero != -1:
        last_total += 1
    if last_total > highest:
        return last_total
    return highest
