from stacks.min_stack import MinStack


def test_min_stack():
    stack = MinStack()
    stack.push(-1)
    stack.push(-2)
    assert stack.get_min() == -2

    stack.push(-3)
    assert stack.get_min() == -3

    stack.pop()
    stack.pop()
    assert stack.get_min() == -1
