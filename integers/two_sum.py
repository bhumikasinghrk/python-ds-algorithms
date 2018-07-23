# Leetcode: https://leetcode.com/problems/two-sum/description/
# # Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# #
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# #
# # Example:
# #
# # Given nums = [2, 7, 11, 15], target = 9,
# #
# # Because nums[0] + nums[1] = 2 + 7 = 9,
# # return [0, 1].


def two_sum(array: [], target: int) -> []:
    complements = dict()

    for index, num in enumerate(array):
        complement = str(target - num)
        if complement in complements:
            return [index, complements[complement]]
        else:
            complements[str(num)] = index
    return [-1, -1]


def two_sum_sorted(array: [], target: int) -> []:
    length = len(array)
    start = 0
    end = length - 1

    while start < end:
        if array[start] + array[end] > target:
            end -= 1
        elif array[start] + array[end] < target:
            start += 1
        else:
            return [start, end]

    return [start, end]
