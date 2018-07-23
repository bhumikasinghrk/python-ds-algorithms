# Find the number of elements that would need to be added so that each array value is separated by one.
# [1,2,3,5] -> 1 #4 needs to be added to the array


def make_array_consecutive(statues: [int]) -> int:
    length = len(statues)
    statuesneeded = 0

    if length <= 1:
        return statuesneeded

    sortedstatues = sorted(statues)

    for i in range(1, length):
        statuesneeded += (sortedstatues[i] - sortedstatues[i - 1]) - 1

    return statuesneeded