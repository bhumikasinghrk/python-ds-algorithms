from arrays.find_index_largest_number import find_index_largest_number


def test_find_index_largest_number():
    numbers = [2, 4, 5, 8, 3]
    assert find_index_largest_number(numbers) == 3
    assert find_index_largest_number([]) == -1
    assert find_index_largest_number([2]) == 2
