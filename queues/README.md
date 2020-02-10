# Queues

* [Moving Average](#moving-average)

## Moving Average

Leetcode: Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

```python
m = MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```

```python
class MovingAverage:

    def __init__(self, size: int):
        self.queue = Queue(maxsize=size)

    def next(self, val: int) -> float:
        if self.queue.full():
            self.queue.get()
        self.queue.put(val)
        return sum(self.queue.queue) / len(self.queue.queue)
```