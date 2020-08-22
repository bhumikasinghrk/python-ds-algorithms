from strings.multiply_strings import multiply_strings


def test_multiply_strings():
    assert multiply_strings('2', '3') == '6'
    assert multiply_strings('123', '456') == '56088'
