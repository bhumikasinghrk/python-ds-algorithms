from data_structures.queue import QueueList


def test_queue_list():
    queue = QueueList()
    assert len(queue) == 0

    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.dequeue() == 1
    assert len(queue) == 0
