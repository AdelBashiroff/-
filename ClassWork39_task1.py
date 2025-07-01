import random
import time
import matplotlib.pyplot as plt

# Генерация n случайных точек
def generate_points(n):
    return [(random.randint(0, 10_000), random.randint(0, 10_000)) for _ in range(n)]

# Построение ломаной
def construct_polyline(points):
    points.sort()  # по x-координате (либо y при необходимости)
    return points

# Среднее время выполнения
def average_time(trials=10, n=1000):
    total_time = 0
    for _ in range(trials):
        pts = generate_points(n)
        start = time.perf_counter()
        _ = construct_polyline(pts)
        end = time.perf_counter()
        total_time += end - start
    avg = total_time / trials
    print(f"Среднее время для n={n}: {avg:.6f} сек")
    return avg


def plot_runtime():
    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000]
    times = [average_time(n=n, trials=5) for n in sizes]

    plt.plot(sizes, times, marker='o')
    plt.title("Время построения ломаной от количества точек")
    plt.xlabel("Количество точек (n)")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()


plot_runtime()
