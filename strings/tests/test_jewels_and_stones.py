from strings.jewels_and_stones import jewels_and_stones


def test_jewels_and_stones():
    assert jewels_and_stones("aA", "aAAbbbb") == 3
