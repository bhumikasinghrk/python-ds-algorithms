from strings.longest_common_prefix import longest_common_prefix


def test_longest_common_prefix():
    arr = ["test", "tester", "testx", "tesk"]
    assert longest_common_prefix(arr) == "tes"

    arr = ["c", "c"]
    assert longest_common_prefix(arr) == "c"
