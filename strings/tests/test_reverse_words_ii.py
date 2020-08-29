from strings.reverse_words_ii import reverse_words_ii


def test_reverse_words_ii():
    sentence = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    reverse_words_ii(sentence)
    assert sentence == ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"]

    sentence = ["h", "i", "!"]
    reverse_words_ii(sentence)
    assert sentence == ["h", "i", "!"]

    sentence = ["a", " ", "b", "o", "y"]
    reverse_words_ii(sentence)
    assert sentence == ["b", "o", "y", " ", "a"]

    sentence = ["a", " ", "b"]
    reverse_words_ii(sentence)
    assert sentence == ["b", " ", "a"]

    sentence = ["a"]
    reverse_words_ii(sentence)
    assert sentence == ["a"]

    sentence = [""]
    reverse_words_ii(sentence)
    assert sentence == [""]
