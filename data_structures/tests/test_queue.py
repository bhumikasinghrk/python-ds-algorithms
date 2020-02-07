from data_structures.queues import QueueList, QueueLinkList


def test_queue_list():
    queue = QueueList()
    assert len(queue) == 0

    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.dequeue() == 1
    assert len(queue) == 0


def test_queue_linked_list():
    queue = QueueLinkList()
    assert len(queue) == 0

    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.dequeue() == 1
    assert len(queue) == 0
