from strings.string_to_integer_ii import string_to_integer_ii


def test_string_to_integer_ii():
    assert string_to_integer_ii("34") == 34
    assert string_to_integer_ii("100") == 100
    assert string_to_integer_ii("-12") == -12
    assert string_to_integer_ii("6") == 6
    assert string_to_integer_ii("0") == 0
    assert string_to_integer_ii("+34") == 34
