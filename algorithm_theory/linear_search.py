def linear_search(array, left, right, target):
    for index in range(left, right + 1):
        if array[index] == target:
            return index
    return None
