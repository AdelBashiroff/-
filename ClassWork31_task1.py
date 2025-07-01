import math
import time


# Рекурсивная функция для вычисления log(N!)
def recursive_log_factorial(N):
    if N == 1:
        return 0  # log(1) = 0, базовый случай
    else:
        return math.log(N) + recursive_log_factorial(N - 1)


# Функция для оценки времени работы алгоритма
def average_runtime(trials=10, size=1000):
    times = []

    for _ in range(trials):
        start = time.perf_counter()
        result = recursive_log_factorial(size)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    avg_time = sum(times) / trials
    print(f"Среднее время выполнения на {trials} запусков (N={size}): {avg_time:.8f} секунд")


# Пример вызова
average_runtime()
