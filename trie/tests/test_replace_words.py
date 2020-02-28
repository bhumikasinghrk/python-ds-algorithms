from trie.replace_words import replace_words


def test_replace_words():
    new_words = ['ca', 'cat', 'battle', 'bat', 'rat']
    sentence = 'the cattle was rattled by the battery'
    output = 'the ca was rat by the bat'
    assert replace_words(new_words, sentence) == output
