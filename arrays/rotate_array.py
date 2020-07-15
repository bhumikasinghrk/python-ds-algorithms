from typing import List


def rotate_array_with_array(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    copy = [0] * length

    for index in range(length):
        copy[(index + k) % length] = nums[index]

    return copy
