#  Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for
#  which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers,
#  return the number for which the second occurrence has a smaller index than the second occurrence of the other number
#  does. If there are no such elements, return -1.


def first_duplicate(array: [int]) -> int:
    number_counter = dict()
    for value in array:
        if value in number_counter:
            number_counter[value] += 1
        else:
            number_counter[value] = 1

    for value in array:
        if number_counter[value] > 1:
            return value
    return -1


def first_duplicate_in_place(array: [int]) -> int:
    while len(array) > 0:
        value = array.pop(0)
        if value in array:
            return value
    return -1
