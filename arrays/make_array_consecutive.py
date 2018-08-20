# Find the number of elements that would need to be added so that each array value is separated by one.
# [1,2,3,5] -> 1 #4 needs to be added to the array


def make_array_consecutive(values: [int]) -> int:
    length = len(values)
    numbers_needed = 0

    if length <= 1:
        return numbers_needed

    sorted_numbers = sorted(values)

    for i in range(1, length):
        numbers_needed += (sorted_numbers[i] - sorted_numbers[i - 1]) - 1

    return numbers_needed