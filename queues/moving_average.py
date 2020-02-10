from queue import Queue
# Leetcode: Moving Average from Data Stream


class MovingAverage:

    def __init__(self, size: int):
        self.queue = Queue(maxsize=size)

    def next(self, val: int) -> float:
        if self.queue.full():
            self.queue.get()
        self.queue.put(val)
        return sum(self.queue.queue) / len(self.queue.queue)
