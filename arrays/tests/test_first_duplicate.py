from arrays.first_duplicate import first_duplicate, first_duplicate_in_place


def test_first_duplicate():
    assert first_duplicate([1, 2, 3]) == -1
    assert first_duplicate([1, 2, 3, 4, 5, 1]) == 1


def test_first_duplicate_in_place():
    assert first_duplicate_in_place([1, 2, 3]) == -1
    assert first_duplicate_in_place([1, 2, 3, 4, 5, 1]) == 1
