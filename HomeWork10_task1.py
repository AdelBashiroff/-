import time
import random
import numpy as np
import matplotlib.pyplot as plt


def gcd_subtraction(a, b):
    # Свойства НОД
    if b == 0:
        return a
    if a == 0:
        return b
    if a < b:
        return gcd_subtraction(b, a)
    return gcd_subtraction(a - b, b)


def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), np.min(times), np.max(times)


sizes = [10 ** i for i in range(1, 7)]  # от 10 до 1_000_000
mean_times = []
min_times = []
max_times = []

for size in sizes:
    a = random.randint(size, size * 10)
    b = random.randint(1, size)

    mean_time, min_time, max_time = measure_time(gcd_subtraction, a, b, repeats=10)
    mean_times.append(mean_time)
    min_times.append(min_time)
    max_times.append(max_time)

    print(f"Размер: {size}")
    print(f"Среднее время: {mean_time:.10f}")
    print(f"Мин. время: {min_time:.10f}")
    print(f"Макс. время: {max_time:.10f}")
    print("------")

# График
plt.figure(figsize=(12, 6))
plt.plot(sizes, mean_times, label="Среднее время", marker='o', color='green')
plt.fill_between(sizes, min_times, max_times, alpha=0.3, color='green', label="Мин/Макс диапазон")

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (секунды)")
plt.title("Время выполнения алгоритма Евклида (через вычитание)")
plt.legend()
plt.grid(True)
plt.show()
