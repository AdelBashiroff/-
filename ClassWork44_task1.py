import random
import time
import matplotlib.pyplot as plt

def max_equal_run_length(A):
    if not A:
        return 0
    max_len = 1
    current_len = 1
    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 1
    return max_len

def average_runtime(length=10000, trials=10):
    total_time = 0
    result = 0
    for _ in range(trials):
        A = [random.randint(0, 5) for _ in range(length)]
        start = time.perf_counter()
        result = max_equal_run_length(A)
        end = time.perf_counter()
        total_time += (end - start)
    avg = total_time / trials
    print(f"N={length}, max_run={result}, среднее время: {avg:.6f} сек")
    return avg

# Построим график
def plot_timings():
    sizes = [10**2, 10**3, 10**4, 10**5, 5*10**5, 10**6]
    times = [average_runtime(n) for n in sizes]
    plt.plot(sizes, times, marker='o')
    plt.title("Время выполнения: макс. длина равных подряд элементов")
    plt.xlabel("Размер входа N")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()

plot_timings()
