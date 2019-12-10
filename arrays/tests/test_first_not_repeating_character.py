from arrays.first_not_repeating_character import first_not_repeating_character, first_not_repeating_character_set


def test_first_not_repeating_character():
    assert first_not_repeating_character('aaaaabc') == 'b'
    assert first_not_repeating_character('aaaaaa') == '_'


def test_first_not_repeating_character_set():
    assert first_not_repeating_character_set('aaaaabc') == 'b'
    assert first_not_repeating_character_set('aaaaaa') == '_'
