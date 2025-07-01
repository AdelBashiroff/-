import time
from collections import deque
import matplotlib.pyplot as plt

def count_paths(N, K):
    if N == 0:
        return 0
    dp = deque([1])  # dp[0] = 1, начальная точка
    total = 1  # сумма последних K элементов
    for i in range(1, N):
        dp.append(total)
        total += dp[-1]
        if len(dp) > K:
            total -= dp.popleft()
    return dp[-1]

# Среднее время выполнения для пары (N, K)
def average_time(n, k, trials=10):
    total_time = 0
    result = 0
    for _ in range(trials):
        start = time.perf_counter()
        result = count_paths(n, k)
        end = time.perf_counter()
        total_time += (end - start)
    avg = total_time / trials
    print(f"N={n:>6}, K={k:>3} → путей: {result}, среднее время: {avg:.6f} сек")
    return avg

# График времени от размера поля
def plot_runtime():
    Ns = [10, 100, 1_000, 5_000, 10_000, 50_000]
    times = [average_time(n, 5) for n in Ns]
    plt.plot(Ns, times, marker='o')
    plt.title("Время работы: число путей фишки (память O(K))")
    plt.xlabel("Длина поля N")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()

plot_runtime()
