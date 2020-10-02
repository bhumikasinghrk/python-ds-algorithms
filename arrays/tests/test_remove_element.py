from arrays.remove_element import remove_element


def test_remove_element():
    arr = [3, 2, 2, 3]
    length = remove_element(arr, 3)
    assert length == 2
    assert arr == [2, 2, 2, 3]

    arr = [1]
    length = remove_element(arr, 1)
    assert length == 0
    assert arr == [1]

    arr = [2, 2, 3, 3]
    length = remove_element(arr, 3)
    assert length == 2
    assert arr == [2, 2, 3, 3]
