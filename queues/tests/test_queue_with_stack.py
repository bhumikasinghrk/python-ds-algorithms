from queues.queue_with_stack import Queue


def test_queue_with_stack():
    queue = Queue()
    assert queue.empty()
    assert queue.push(1) is None
    queue.push(2)
    assert queue.peek() == 1
    assert not queue.empty()
    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.empty()
