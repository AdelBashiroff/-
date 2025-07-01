import time
import random

def find_missing_number(arr):
    n = len(arr)
    expected_sum = (n * (n + 1)) // 2  # n+1 чисел всего, но один отсутствует => arr длины n
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def average_runtime(trials=10, size=100_000):
    times = []

    for _ in range(trials):
        full = list(range(size + 1))
        missing = random.randint(0, size)
        full.remove(missing)
        random.shuffle(full)

        start = time.perf_counter()
        result = find_missing_number(full)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    avg_time = sum(times) / trials
    print(f"Среднее время выполнения на {trials} запусков (n={size}): {avg_time:.8f} секунд")
