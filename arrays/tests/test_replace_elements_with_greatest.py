from arrays.replace_elements_with_greatest import replace_elements_with_greatest


def test_replace_elements_with_greatest():
    assert replace_elements_with_greatest([1, 2]) == [2, -1]
    assert replace_elements_with_greatest([1]) == [-1]
    assert replace_elements_with_greatest([17, 18, 5, 6, 6, 2, 1]) == [18, 6, 6, 6, 2, 1, -1]
    assert replace_elements_with_greatest([1, 1]) == [1, -1]
