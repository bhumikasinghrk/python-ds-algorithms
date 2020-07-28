from typing import List


def rotate_array_with_array(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    copy = [0] * length

    for index in range(length):
        copy[(index + k) % length] = nums[index]

    return copy


def rotate_array_in_place(nums: List[int], k: int) -> List[int]:
    length = len(nums)
    k = k % length

    reverse(nums, 0, length - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, length - 1)
    return nums


def reverse(arr: List, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
