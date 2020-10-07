from strings.implement_str_str import str_str


def test_str_str():
    assert str_str('hello', 'll') == 2
    assert str_str('test', '') == 0
    assert str_str('foo', 'bar') == -1
    assert str_str('a', 'aa') == -1
    assert str_str('aaa', 'a') == 0
