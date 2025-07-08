import time
import matplotlib.pyplot as plt

def gray_code(n):
    codes = []
    for i in range(2 ** n):
        gray = i ^ (i >> 1)
        codes.append(format(gray, f'0{n}b'))
    return codes

def measure_time(func, n, repeats=5):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        times.append(end - start)
    return min(times), max(times), sum(times) / repeats

# Проверяем от N = 1 до 20
Ns = list(range(1, 21))
min_times = []
max_times = []
avg_times = []

for n in Ns:
    min_t, max_t, avg_t = measure_time(gray_code, n)
    min_times.append(min_t)
    max_times.append(max_t)
    avg_times.append(avg_t)
    print(f"N={n:2d} | Среднее время: {avg_t:.8f} с | Мин: {min_t:.8f} с | Макс: {max_t:.8f} с")

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(Ns, avg_times, label="Среднее время", marker='o', color='green')
plt.fill_between(Ns, min_times, max_times, alpha=0.2, color='green', label="Мин/Макс")

plt.xlabel("Длина кода Грея (N)")
plt.ylabel("Время выполнения (сек)")
plt.title("Зависимость времени генерации кода Грея от N")
plt.legend()
plt.grid(True)
plt.yscale("log")  # т.к. время растёт экспоненциально
plt.show()
