import bisect
import time
import random

def lis_length(arr):
    if not arr:
        return 0

    tails = []

    for x in arr:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x

    return len(tails)

def average_runtime_lis(trials=10, size=10_000):
    times = []
    for _ in range(trials):
        arr = [random.randint(0, 10_000) for _ in range(size)]
        start = time.perf_counter()
        lis_length(arr)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = sum(times) / trials
    print(f"Среднее время для LIS (размер {size}, {trials} запусков): {avg_time:.6f} сек")
