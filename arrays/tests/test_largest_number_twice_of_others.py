from arrays.largest_number_at_least_twice_of_others import largest_number_at_least_twice_of_others, \
    largest_number_at_least_twice_of_others2


def test_largest_number_at_least_twice_of_others():
    assert largest_number_at_least_twice_of_others([1, 0]) == 0
    assert largest_number_at_least_twice_of_others([3, 6, 1, 0]) == 1
    assert largest_number_at_least_twice_of_others([0, 0, 3, 2]) == -1
    assert largest_number_at_least_twice_of_others([3, 0, 0, 2]) == -1
    assert largest_number_at_least_twice_of_others([0, 0, 1, 2]) == 3
    assert largest_number_at_least_twice_of_others([0]) == 0


def test_largest_number_at_least_twice_of_others2():
    assert largest_number_at_least_twice_of_others2([1, 0]) == 0
    assert largest_number_at_least_twice_of_others2([3, 6, 1, 0]) == 1
    assert largest_number_at_least_twice_of_others2([0, 0, 3, 2]) == -1
    assert largest_number_at_least_twice_of_others2([3, 0, 0, 2]) == -1
    assert largest_number_at_least_twice_of_others2([0, 0, 1, 2]) == 3
    assert largest_number_at_least_twice_of_others2([0]) == 0
