import time
import matplotlib.pyplot as plt
from statistics import mean

def count_occurrences(b, p, a, d):
    count = 0
    for c in range(1, d + 1):
        if (b * c) % p == a:
            count += 1
    return count

# Запуск на разных значениях d
ds = [10**i for i in range(1, 7)]  # от 10 до 1_000_000
b = 17
p = 9973
a = 42
repeats = 10

times = []

for d in ds:
    durations = []
    for _ in range(repeats):
        start = time.time()
        count_occurrences(b, p, a, d)
        end = time.time()
        durations.append(end - start)
    times.append({
        "d": d,
        "avg": mean(durations),
        "min": min(durations),
        "max": max(durations)
    })

# Печать таблицы
print(f"{'d':>10} | {'avg':>10} | {'min':>10} | {'max':>10}")
print("-" * 45)
for t in times:
    print(f"{t['d']:10} | {t['avg']:.6f} | {t['min']:.6f} | {t['max']:.6f}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot([t['d'] for t in times], [t['avg'] for t in times], marker='o', label='Среднее время')
plt.plot([t['d'] for t in times], [t['min'] for t in times], linestyle='--', label='Минимальное время')
plt.plot([t['d'] for t in times], [t['max'] for t in times], linestyle='--', label='Максимальное время')
plt.xlabel("d (число итераций)")
plt.ylabel("Время выполнения (сек)")
plt.title("Время работы count_occurrences в зависимости от d")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
