import random
import time
import numpy as np
import matplotlib.pyplot as plt

# Алгоритм Евклида: деление с остатком
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Алгоритм Евклида: вычитание
def gcd2(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a or b

# Функция замера времени
def measure_time(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.perf_counter()
        func(*args)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times), np.min(times), np.max(times)

# Список размеров (чисел от 10 до 1_000_000)
sizes = [10 ** i for i in range(1, 7)]

# Хранилища результатов
time_gcd_mean = []
time_gcd_min = []
time_gcd_max = []

time_gcd2_mean = []
time_gcd2_min = []
time_gcd2_max = []

# Замеры
for size in sizes:
    a = random.randint(size, 10 * size)
    b = random.randint(1, size)

    mean_gcd, min_gcd, max_gcd = measure_time(gcd, a, b)
    time_gcd_mean.append(mean_gcd)
    time_gcd_min.append(min_gcd)
    time_gcd_max.append(max_gcd)

    mean_gcd2, min_gcd2, max_gcd2 = measure_time(gcd2, a, b)
    time_gcd2_mean.append(mean_gcd2)
    time_gcd2_min.append(min_gcd2)
    time_gcd2_max.append(max_gcd2)

    print(f"Размер: {size}")
    print(f"GCD (деление): среднее={mean_gcd:.10f}, мин={min_gcd:.10f}, макс={max_gcd:.10f}")
    print(f"GCD2 (вычитание): среднее={mean_gcd2:.10f}, мин={min_gcd2:.10f}, макс={max_gcd2:.10f}")
    print("------")

# Построение графика
plt.figure(figsize=(12, 6))

plt.plot(sizes, time_gcd_mean, label="GCD (деление с остатком)", marker='o', color='blue')
plt.fill_between(sizes, time_gcd_min, time_gcd_max, alpha=0.2, color='blue')

plt.plot(sizes, time_gcd2_mean, label="GCD2 (вычитание)", marker='o', color='orange')
plt.fill_between(sizes, time_gcd2_min, time_gcd2_max, alpha=0.2, color='orange')

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Размер чисел")
plt.ylabel("Время выполнения (секунды)")
plt.title("Сравнение алгоритмов Евклида: деление vs вычитание")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
