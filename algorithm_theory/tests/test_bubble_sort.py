from algorithm_theory.bubble_sort import bubble_sort

def test_bubble_sort():
    a = [6, 3, 4, 5, 2, 1]
    assert bubble_sort(a) == [1, 2, 3, 4, 5, 6]

    a = [2, 1]
    assert bubble_sort(a) == [1, 2]

    a = [1]
    assert bubble_sort(a) == [1]

    a = []
    assert bubble_sort(a) == []

#test_bubble_sort()