from strings.first_unique_character_in_str import first_unique_character_in_str


def test_first_unique_character():
    string = 'abc'
    assert first_unique_character_in_str(string) == 0

    string = 'eee'
    assert first_unique_character_in_str(string) == -1

    string = 'aba'
    assert first_unique_character_in_str(string) == 1
