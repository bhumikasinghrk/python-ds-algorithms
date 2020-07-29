from strings.anagram import valid_anagram


def test_valid_anagram():
    assert valid_anagram("car", "rac")
    assert not valid_anagram("test", "tests")
    assert not valid_anagram("test", "tezt")
