from stacks.valid_parentheses import valid_parentheses


def test_valid_parentheses():
    assert valid_parentheses('()')
    assert valid_parentheses('(){}[]')
    assert valid_parentheses('{[]}')
    assert not valid_parentheses('(]')
    assert not valid_parentheses('((')
    assert not valid_parentheses('([)]')
