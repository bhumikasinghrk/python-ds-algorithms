# Jump Search is a searching algorithm for sorted arrays. The basic idea is to check fewer elements (than linear search)
# by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
#
# step size is m = √n.

import math
from algorithm_theory.linear_search import linear_search
from typing import Optional


def jump_search(array: [int], target: int) -> Optional[int]:
    length = len(array)
    interval = int(math.sqrt(length))
    index = interval - 1  # 0 Based
    previous = index

    while index <= length - 1:
        if array[index] == target:
            return index
        elif array[index] > target:
            return linear_search(array, previous, index - 1, target)
        else:
            previous = index
            index += interval

    return None
