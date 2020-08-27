from strings.reverse_words import reverse_words


def test_reverse_words():
    assert reverse_words('foo bar baz') == 'oof rab zab'
    assert reverse_words('foo') == 'oof'
    assert reverse_words('') == ''
    assert reverse_words('a b') == 'a b'
