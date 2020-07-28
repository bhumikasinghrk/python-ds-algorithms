from typing import List


def intersection_of_two_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
    intersection = []
    nums1_map = {}

    for num in nums1:
        if num in nums1_map:
            nums1_map[num] += 1
        else:
            nums1_map[num] = 1

    for num in nums2:
        if num in nums1_map and nums1_map[num] > 0:
            intersection.append(num)
            nums1_map[num] -= 1

    return intersection
