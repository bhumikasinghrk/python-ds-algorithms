from typing import List


def merge_sorted_array(nums1: List[int], nums1_length: int, nums2: List[int], nums2_length: int) -> List[int]:
    index_nums1 = nums1_length - 1
    index_nums2 = nums2_length - 1
    current_index = nums1_length + nums2_length - 1

    while index_nums2 >= 0:
        if index_nums1 < 0 <= index_nums2:
            nums1[current_index] = nums2[index_nums2]
            index_nums2 -= 1
        elif nums1[index_nums1] > nums2[index_nums2]:
            nums1[current_index] = nums1[index_nums1]
            index_nums1 -= 1
        else:
            nums1[current_index] = nums2[index_nums2]
            index_nums2 -= 1

        current_index -= 1

    return nums1
