from typing import List
from _collections import deque


def daily_temperatures_brute_force(temps: List[int]) -> List[int]:
    daily_temps = []
    for index, temp in enumerate(temps):
        count = 0
        for sub_index in range(index + 1, len(temps)):
            count += 1
            if temps[sub_index] > temp:
                break
            if sub_index == len(temps) - 1:
                count = 0
        daily_temps.append(count)
    return daily_temps


def daily_temperatures(temps: List[int]) -> List[int]:
    daily_temps = deque()
    stack = []

    for index in range(len(temps) - 1, -1, -1):
        while stack and temps[index] >= temps[stack[-1]]:
            stack.pop()

        if stack:
            daily_temps.appendleft(stack[-1] - index)
        else:
            daily_temps.appendleft(0)
        stack.append(index)
    return list(daily_temps)
