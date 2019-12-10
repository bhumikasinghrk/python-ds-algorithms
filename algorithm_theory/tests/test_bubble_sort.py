from algorithm_theory.bubble_sort import bubble_sort


def test_bubble_sort():
    arr = [6, 3, 4, 5, 2, 1]
    assert bubble_sort(arr) == [1, 2, 3, 4, 5, 6]

    arr = [2, 1]
    assert bubble_sort(arr) == [1, 2]

    arr = [1]
    assert bubble_sort(arr) == [1]

    arr = []
    assert bubble_sort(arr) == []
