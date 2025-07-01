import time
import random

def gcd_subtraction(a, b):
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a or b

def gcd_mod(a, b):
    while b:
        a, b = b, a % b
    return a

def measure_time(func, iterations=100, max_value=1_000_000):
    total_time = 0.0
    for _ in range(iterations):
        a = random.randint(10, max_value)
        b = random.randint(10, max_value)
        start = time.perf_counter()
        func(a, b)
        end = time.perf_counter()
        total_time += end - start
    return total_time / iterations

# Запускаем замеры
iters = 100
print(f"Среднее время за {iters} запусков (max=1_000_000):")

avg_sub = measure_time(gcd_subtraction, iters, 1_000_000)
avg_mod = measure_time(gcd_mod, iters, 1_000_000)

print(f"Алгоритм вычитания: {avg_sub:.8f} сек")
print(f"Алгоритм через остаток: {avg_mod:.8f} сек")
