from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    length = len(nums)
    first_positive = None

    for index in range(length):
        if nums[index] >= 0:
            first_positive = index
            break

    # All Negative
    if first_positive is None:
        result = []
        for index in range(length - 1, -1, -1):
            result.append(nums[index] * nums[index])
        return result

    # All Positive
    if first_positive == 0:
        return [x * x for x in nums]

    left = first_positive - 1
    right = first_positive
    squares = []

    while left >= 0 or right < length:
        if left >= 0 and right < length:
            if abs(nums[left]) < nums[right]:
                squares.append(nums[left] * nums[left])
                left -= 1
            else:
                squares.append(nums[right] * nums[right])
                right += 1
        elif right < length:
            squares.append(nums[right] * nums[right])
            right += 1
        elif left >= 0:
            squares.append(nums[left] * nums[left])
            left -= 1

    return squares
