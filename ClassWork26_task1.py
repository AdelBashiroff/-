import time
import matplotlib.pyplot as plt

# Функция нахождения целой части квадратного корня
def integer_sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid > x // mid:
            right = mid - 1
        else:
            left = mid + 1
    return right

# Тестирование и замер времени
import numpy as np

xs = np.logspace(1, 12, num=30, base=10, dtype=int)  # от 10 до 1e12
times = []

for x in xs:
    t0 = time.time()
    for _ in range(100):
        integer_sqrt(x)
    t1 = time.time()
    avg_time = (t1 - t0) / 100
    times.append(avg_time)

# Построение графика
plt.plot(xs, times, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("x")
plt.ylabel("Время выполнения (сек)")
plt.title("Зависимость времени выполнения integer_sqrt(x) от x")
plt.grid(True)
plt.show()
