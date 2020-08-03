from strings.palindrome import valid_palindrome, valid_palindrome_naive


def test_valid_palindrome_naive():
    val1 = 'aba'
    val2 = 'aacbaa'
    val3 = 'a:bba'

    assert valid_palindrome_naive(val1)
    assert not valid_palindrome_naive(val2)
    assert not valid_palindrome_naive(val3)


def test_valid_palindrome():
    val1 = 'aba'
    val2 = 'aacbaa'
    val3 = 'a:bba'

    assert valid_palindrome(val1)
    assert not valid_palindrome(val2)
    assert valid_palindrome(val3)
