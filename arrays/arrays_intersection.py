from typing import List


# Leetcode 1213. Intersection of Three Sorted Arrays

def arrays_intersection(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    intersection = set(arr1)
    intersection = intersection.intersection(arr2)
    return list(intersection.intersection(arr3))


def arrays_intersection2(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    index1 = 0
    index2 = 0
    index3 = 0
    result = []

    while index1 < len(arr1) and index2 < len(arr2) and index3 < len(arr3):
        if arr1[index1] == arr2[index2] == arr3[index3]:
            result.append(arr1[index1])
            index1 += 1
            index2 += 1
            index3 += 1
            continue

        current_max = max(arr1[index1], arr2[index2], arr3[index3])

        if arr1[index1] < current_max:
            index1 += 1
        if arr2[index2] < current_max:
            index2 += 1
        if arr3[index3] < current_max:
            index3 += 1

    return result
