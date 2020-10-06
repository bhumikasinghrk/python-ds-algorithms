from strings.add_binary import add_binary, add_binary_with_builtins


def test_add_binary():
    assert add_binary("1", "1") == "10"
    assert add_binary("10", "1") == "11"
    assert add_binary("101", "11") == "1000"
    assert add_binary("1011", "1101") == "11000"


def test_add_binary_builtins():
    assert add_binary_with_builtins("1", "1") == "10"
    assert add_binary_with_builtins("10", "1") == "11"
    assert add_binary_with_builtins("101", "11") == "1000"
    assert add_binary_with_builtins("1011", "1101") == "11000"
