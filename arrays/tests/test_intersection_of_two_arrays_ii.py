from arrays.intersection_of_two_arrays_ii import intersection_of_two_arrays


def test_intersection_of_two_arrays():
    arr = [1, 2, 2, 1]
    arr2 = [2, 2]
    assert intersection_of_two_arrays(arr, arr2) == [2, 2]
    assert intersection_of_two_arrays(arr2, arr) == [2, 2]

    arr = [1, 2, 3, 4, -2]
    arr2 = [-2, 4, 6, 3]
    assert sorted(intersection_of_two_arrays(arr, arr2)) == [-2, 3, 4]
    assert sorted(intersection_of_two_arrays(arr2, arr)) == [-2, 3, 4]
