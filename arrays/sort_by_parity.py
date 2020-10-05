from typing import List


def sort_by_parity(nums: List[int]) -> List[int]:
    length = len(nums)
    left_index = 0
    right_index = length - 1

    while left_index < right_index:
        if nums[left_index] % 2 == 0:
            left_index += 1
        elif nums[right_index] % 2 != 0:
            right_index -= 1
        else:
            nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
            left_index += 1
            right_index -= 1
    return nums
