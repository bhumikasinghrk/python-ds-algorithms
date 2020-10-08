from strings.longest_common_prefix import longest_common_prefix_horizontal, longest_common_prefix_vertical


def test_longest_common_prefix_horizontal():
    assert longest_common_prefix_horizontal(["acv", "def", "sgh"]) == ""
    assert longest_common_prefix_horizontal(["abab", ""]) == ""
    assert longest_common_prefix_horizontal(["ababaabbab", "abab", "abbaba"]) == "ab"
    assert longest_common_prefix_horizontal(["c", "c"]) == "c"
    assert longest_common_prefix_horizontal(["a", "aa", "aaa"]) == "a"
    assert longest_common_prefix_horizontal(["aaa", "aa", "a"]) == "a"


def test_longest_common_prefix_vertical():
    assert longest_common_prefix_vertical(["acv", "def", "sgh"]) == ""
    assert longest_common_prefix_vertical(["abab", ""]) == ""
    assert longest_common_prefix_vertical(["ababaabbab", "abab", "abbaba"]) == "ab"
    assert longest_common_prefix_vertical(["c", "c"]) == "c"
    assert longest_common_prefix_vertical(["a", "aa", "aaa"]) == "a"
    assert longest_common_prefix_vertical(["aaa", "aa", "a"]) == "a"

