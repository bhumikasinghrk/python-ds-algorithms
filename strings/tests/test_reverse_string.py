from strings.reverse_string import reverse_string, reverse_string_in_place, reverse_string_with_list_comprehension, reverse_string_with_loop


def test_reverse_string():
    assert reverse_string('test') == 'tset'


def test_reverse_string_inplace():
    string = ['t', 'e', 's', 't']
    reverse_string_in_place(string)
    assert string == ['t', 's', 'e', 't']


def test_reverse_string_with_list_comprehension():
    assert reverse_string_with_list_comprehension('test') == 'tset'


def test_reverse_with_loop():
    assert reverse_string_with_loop('test') == 'tset'
