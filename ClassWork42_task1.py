import random
import time
import matplotlib.pyplot as plt

# Рекурсивная функция "разделяй и властвуй"
def find_max_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_max = find_max_divide_conquer(arr, left, mid)
    right_max = find_max_divide_conquer(arr, mid + 1, right)
    return max(left_max, right_max)

# Среднее время работы для одного размера массива
def average_time(n, trials=10):
    total_time = 0
    for _ in range(trials):
        arr = [random.randint(-10**6, 10**6) for _ in range(n)]
        start = time.perf_counter()
        _ = find_max_divide_conquer(arr, 0, len(arr) - 1)
        end = time.perf_counter()
        total_time += (end - start)
    avg = total_time / trials
    print(f"n={n:>7} → среднее время: {avg:.6f} сек")
    return avg

# График зависимости времени от размера массива
def plot_runtime():
    sizes = [100, 1_000, 5_000, 10_000, 50_000, 100_000, 200_000]
    times = [average_time(n) for n in sizes]
    plt.plot(sizes, times, marker='o')
    plt.title("Время работы рекурсивного поиска максимума (разделяй и властвуй)")
    plt.xlabel("Размер массива (n)")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()

plot_runtime()
