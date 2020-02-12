# Queues

* [Implement Queue With Stack](#implement-queue-with-stack)
* [Moving Average](#moving-average)

## Implement Queue With Stack

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.


Example:

```python
queue = MyQueue()

queue.push(1)
queue.push(2)  
queue.peek()  # returns 1
queue.pop()   # returns 1
queue.empty() # returns false
```

```python
class Queue(Generic[T]):
    def __init__(self):
        self.queue = deque()

    def push(self, item: T) -> None:
        self.queue.append(item)

    def pop(self) -> T:
        return self.queue.popleft()

    def peek(self) -> T:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
```


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