from arrays.make_array_consecutive import make_array_consecutive


def test_make_array_consecutive():
    arr = [6, 2, 3, 8]
    assert make_array_consecutive(arr) == 3
