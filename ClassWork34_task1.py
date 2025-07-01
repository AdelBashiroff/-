import time
import random


def sort_012(arr):
    low = mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


def average_runtime(trials=10, size=1_000_000):
    times = []

    for _ in range(trials):
        arr = [random.choice([0, 1, 2]) for _ in range(size)]
        start = time.perf_counter()
        sort_012(arr)
        end = time.perf_counter()
        times.append(end - start)

    avg_time = sum(times) / trials
    print(f"Среднее время работы на {trials} запусков (массив из {size} элементов): {avg_time:.6f} сек")


# Пример вызова
average_runtime()
