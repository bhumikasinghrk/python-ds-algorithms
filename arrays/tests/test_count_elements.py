from arrays.count_elements import count_elements


def test_count_elements():
    assert count_elements([1, 2, 3]) == 2
    assert count_elements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert count_elements([1, 3, 2, 3, 5, 0]) == 3
    assert count_elements([1, 1, 2, 2]) == 2
