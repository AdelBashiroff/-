import time
import random
from collections import deque

# Вариант 1: С использованием deque
def merge_sorted_deques(q1, q2):
    result = deque()
    while q1 and q2:
        if q1[0] <= q2[0]:
            result.append(q1.popleft())
        else:
            result.append(q2.popleft())
    result.extend(q1)
    result.extend(q2)
    return result

# Вариант 2: Очередь через два стека
class QueueTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        return None

    def peek(self):
        val = self.dequeue()
        if val is not None:
            self.stack_out.append(val)
        return val

    def empty(self):
        return not (self.stack_in or self.stack_out)

# Объединение очередей на двух стеках
def merge_queue_stacks(q1, q2):
    result = QueueTwoStacks()
    while not q1.empty() and not q2.empty():
        if q1.peek() <= q2.peek():
            result.enqueue(q1.dequeue())
        else:
            result.enqueue(q2.dequeue())
    while not q1.empty():
        result.enqueue(q1.dequeue())
    while not q2.empty():
        result.enqueue(q2.dequeue())
    return result


def test_average_time(n=10, size=1000):
    deque_times = []
    stackq_times = []

    for _ in range(n):
        a = sorted(random.sample(range(size * 2), size))
        b = sorted(random.sample(range(size * 2), size))

        # Для deque
        dq1 = deque(a)
        dq2 = deque(b)
        start = time.perf_counter()
        merge_sorted_deques(deque(dq1), deque(dq2))
        deque_times.append(time.perf_counter() - start)

        # Для очереди через два стека
        q1 = QueueTwoStacks()
        q2 = QueueTwoStacks()
        for x in a:
            q1.enqueue(x)
        for x in b:
            q2.enqueue(x)
        start = time.perf_counter()
        merge_queue_stacks(q1, q2)
        stackq_times.append(time.perf_counter() - start)

    avg_deque = sum(deque_times) / n
    avg_stack = sum(stackq_times) / n

    print(f"Среднее время (deque): {avg_deque:.6f} сек")
    print(f"Среднее время (2 стека): {avg_stack:.6f} сек")
