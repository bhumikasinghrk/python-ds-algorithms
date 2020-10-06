from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    # O(N), O(N)
    unique_nums = set(nums)
    length = len(nums)
    disappeared_nums = []

    for num in range(1, length + 1):
        if num not in unique_nums:
            disappeared_nums.append(num)
    return disappeared_nums


def find_disappeared_numbers_ii(nums: List[int]) -> List[int]:
    # O(N) O(1)
    length = len(nums)

    for index in range(length):
        num_index = abs(nums[index]) - 1
        if nums[num_index] > 0:
            nums[num_index] *= -1

    disappeared_nums = []

    for index in range(length):
        if nums[index] > 0:
            disappeared_nums.append(index + 1)
    return disappeared_nums
