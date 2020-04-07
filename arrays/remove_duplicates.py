from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    last_index = 0
    count = 1

    for index in range(1, len(nums)):
        if nums[index] == nums[last_index]:
            continue
        count += 1
        last_index += 1
        nums[last_index] = nums[index]

    return count
