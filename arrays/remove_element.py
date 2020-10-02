from typing import List


def remove_element(nums: List[int], val: int) -> int:
    index = 0
    count = 0
    length = len(nums)

    while index < length:
        if nums[index] == val:
            count += 1
        else:
            nums[index - count] = nums[index]
        index += 1
    return length - count
