from typing import List


def single_number(nums: List[int]) -> int:
    if not nums:
        return 0

    nums_dict = dict()

    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1

    for num in nums_dict:
        if nums_dict[num] == 1:
            return num

    return 0


def single_number_bitwise(nums: List[int]) -> int:
    if not nums:
        return 0
    current = nums[0]

    for index in range(1, len(nums)):
        current ^= nums[index]

    return current
