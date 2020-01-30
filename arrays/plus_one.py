from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """
    Increment array of digits by one as if a number
    [1, 2, 3] -> [1, 2, 4]

    :param digits: list of int numbers representing a non-negative number
    :return: incremented list
    """

    for i in reversed(range(len(digits))):
        digits[i] = (digits[i] + 1) % 10
        if digits[i] != 0:
            break
        if i == 0:
            digits.insert(0, 1)
            break
    return digits
