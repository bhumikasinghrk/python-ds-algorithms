from typing import List


def move_zeros(nums: List[int]) -> None:
    if not nums or len(nums) == 0:
        return

    current_index = 0
    last_num = None

    while current_index < len(nums):
        if nums[current_index] == 0:
            next_num = last_num if last_num else current_index + 1
            while next_num < len(nums):
                if nums[next_num] != 0:
                    nums[next_num], nums[current_index] = nums[current_index], nums[next_num]
                    last_num = next_num + 1
                    break
                next_num += 1
        current_index += 1
