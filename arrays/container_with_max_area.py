from typing import List


def container_with_max_area(height: List[int]) -> int:
    length = len(height)
    left = 0
    right = length - 1
    max_area = 0

    while left < right:
        lowest = min(height[left], height[right])
        max_area = max(max_area, lowest * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
