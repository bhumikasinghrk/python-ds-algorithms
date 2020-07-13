

def two_sum(array: [int], target: int) -> [int]:
    complements = dict()

    for index, number in enumerate(array):
        complement = target - number
        if complement in complements:
            return [complements[complement], index]
        complements[number] = index

    return [-1, -1]


def two_sum_sorted(array: [int], target: int) -> [int]:
    length = len(array)
    start = 0
    end = length - 1

    while start < end:
        if array[start] + array[end] > target:
            end -= 1
        elif array[start] + array[end] < target:
            start += 1
        else:
            return [start, end]

    return [start, end]
