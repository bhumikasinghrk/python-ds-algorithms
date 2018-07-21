# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in
# wrong order.

def bubble_sort(array):
    length = len(array)

    # Return if nothing to sort
    if length <= 1:
        return array

    # Reduce the upper limit with each iteration, since the correct value has 'bubbled' to the top
    for i in reversed(range(0, length)):
        swap = False
        # Compare value and switch up to the upper limit 'i'
        for j in range(0, i):
            next = j + 1
            if next < length and array[j] > array[next]:
                temp = array[j]
                array[j] = array[next]
                array[next] = temp
                swap = True

        # Return if no swaps take place
        if not swap:
            return array
    return array

