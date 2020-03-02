from typing import List


def find_index_largest_number(numbers: List[int]) -> int:
    if not numbers:
        return -1

    largest_index = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] > numbers[largest_index]:
            largest_index = index
    return largest_index
