from arrays.remove_duplicates import remove_duplicates


def test_remove_duplicates():
    nums = [1, 1, 2]
    assert remove_duplicates(nums) == 2
    assert nums == [1, 2, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
