from typing import List


def remove_duplicates(nums: List[int]) -> int:
    length = len(nums)
    if length <= 1:
        return length

    last_index = 0

    for index in range(1, length):
        if nums[index] == nums[last_index]:
            continue
        last_index += 1
        nums[last_index] = nums[index]

    return last_index + 1
