import bisect
import random
import time

# Бинарный поиск: находим левую и правую границу
def find_bounds(arr, a):
    def lower_bound():
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < a:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound():
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= a:
                left = mid + 1
            else:
                right = mid
        return left - 1

    low = lower_bound()
    if low == len(arr) or arr[low] != a:
        return 0  # a не найден
    high = upper_bound()
    return low, high

def test_bounds_average_time(trials=10, size=100_000):
    times = []

    for _ in range(trials):
        arr = sorted(random.choices(range(5000), k=size))  # допускаются дубликаты
        a = random.choice(arr) if random.random() < 0.8 else -1  # 80% шанс, что элемент есть

        start = time.perf_counter()
        find_bounds(arr, a)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    avg_time = sum(times) / trials
    print(f"Среднее время выполнения (на {trials} запусков): {avg_time:.8f} секунд")
