from arrays.move_zeros import move_zeros


def test_move_zeros():
    arr = [0, 1, 2, 4, 0, 12, 0]
    move_zeros(arr)
    assert arr == [1, 2, 4, 12, 0, 0, 0]
