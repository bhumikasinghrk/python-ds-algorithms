from typing import List


def peaks(numbers: List[int]) -> List[int]:
    length = len(numbers)
    peak_nums = []

    if length < 3:
        return peak_nums

    for index in range(1, length - 1):
        if numbers[index - 1] < numbers[index] and numbers[index] > numbers[index + 1]:
            peak_nums.append(numbers[index])

    return peak_nums
