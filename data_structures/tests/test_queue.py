from data_structures.queues import CircularQueue, QueueList, QueueLinkedList


def test_queue_list():
    queue = QueueList()
    assert len(queue) == 0

    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.dequeue() == 1
    assert len(queue) == 0


def test_queue_linked_list():
    queue = QueueLinkedList()
    assert len(queue) == 0

    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.dequeue() == 1
    assert len(queue) == 0


def test_circular_queue():
    queue = CircularQueue(4)
    assert queue.isempty()
    queue.enqueue(3)
    queue.enqueue(9)
    queue.enqueue(5)
    queue.enqueue(0)
    assert queue.isfull()
    assert not queue.enqueue(5)
    queue.dequeue()
    queue.dequeue()
    assert not queue.isempty()
    assert queue.rear() == 0
    assert queue.front() == 5
