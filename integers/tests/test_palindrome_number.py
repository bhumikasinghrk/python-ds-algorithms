from integers.palindrome_number import is_palindrome


def test_is_palindrome():
    assert is_palindrome(121)
    assert not is_palindrome(-121)
