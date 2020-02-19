from arrays.arrays_intersection import arrays_intersection, arrays_intersection2


def test_arrays_intersection():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [2, 3, 4, 5]
    assert arrays_intersection(arr1, arr2, arr3) == [2, 5]


def test_arrays_intersection2():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [2, 3, 4, 5]
    assert arrays_intersection2(arr1, arr2, arr3) == [2, 5]

