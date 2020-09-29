from strings.longest_substring_without_duplicates import longest_substring_without_duplicates


def test_longest_substring_without_duplicates():
    assert longest_substring_without_duplicates('abcabcbb') == 3
    assert longest_substring_without_duplicates('abc') == 3
    assert longest_substring_without_duplicates('abca') == 3
    assert longest_substring_without_duplicates('abadc') == 4
