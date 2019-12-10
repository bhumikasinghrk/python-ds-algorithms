from arrays.make_array_consecutive import *


def test_make_array_consecutive():
    a = [6, 2, 3, 8]
    assert make_array_consecutive(a) == 3
