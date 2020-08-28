from strings.valid_word_abbreviation import valid_word_abbreviation


def test_valid_word_abbreviation():
    assert not valid_word_abbreviation("apple", "a2e")
    assert valid_word_abbreviation("internationalization", "i12iz4n")
    assert valid_word_abbreviation("internationalization", "i18n")
    assert not valid_word_abbreviation("a", "01")
    assert not valid_word_abbreviation("oil", "01il")
