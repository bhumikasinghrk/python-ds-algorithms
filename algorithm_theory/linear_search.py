def linear_search(array, length, target):
    for index in range(0, length):
        if array[index] == target:
            return index
    return None
