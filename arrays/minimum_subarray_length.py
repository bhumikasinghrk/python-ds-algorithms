from typing import List


def minimum_subarray_length(target: int, numbers: List[int]) -> int:
    answer = None
    left = 0
    total = 0

    for index, _ in enumerate(numbers):
        total += numbers[index]
        while total >= target:
            if answer:
                answer = min(answer, index + 1 - left)
            else:
                answer = index + 1 - left
            total -= numbers[left]
            left += 1

    return answer if answer else 0
