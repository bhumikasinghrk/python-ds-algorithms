from stacks.stack_with_queue import Stack


def test_stack_with_queue():
    stack = Stack()
    assert stack.empty()
    assert stack.push(0) is None
    stack.push(1)
    assert not stack.empty()
    assert stack.top() == 1
    assert stack.pop() == 1
    assert stack.top() == 0
    stack.pop()
    assert stack.empty()
