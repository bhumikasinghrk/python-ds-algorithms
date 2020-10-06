from typing import List


def third_max(nums: List[int]) -> int:
    unique_nums = set(nums)

    if len(unique_nums) < 3:
        return max(unique_nums)

    unique_nums.remove(max(unique_nums))    # 1st
    unique_nums.remove(max(unique_nums))    # 2nd
    return max(unique_nums)                 # 3rd
