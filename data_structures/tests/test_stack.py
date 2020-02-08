from data_structures.stack import StackList


def test_stack():
    stack = StackList()
    assert len(stack) == 0

    stack.push(1)
    assert len(stack) == 1
    assert stack.pop() == 1
