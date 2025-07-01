import random
import time
import math
import matplotlib.pyplot as plt


def euclidean(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair


def closest_split_pair(px, py, delta, best_pair):
    mid_x = px[len(px) // 2][0]
    sy = [p for p in py if abs(p[0] - mid_x) < delta]

    min_dist = delta
    for i in range(len(sy)):
        for j in range(i + 1, min(i + 7, len(sy))):
            p, q = sy[i], sy[j]
            dist = euclidean(p, q)
            if dist < min_dist:
                min_dist = dist
                best_pair = (p, q)
    return min_dist, best_pair


def closest_pair_recursive(px, py):
    if len(px) <= 3:
        return brute_force(px)

    mid = len(px) // 2
    Qx = px[:mid]
    Rx = px[mid:]

    midpoint = px[mid][0]
    Qy = [p for p in py if p[0] <= midpoint]
    Ry = [p for p in py if p[0] > midpoint]

    (dl, pair_l) = closest_pair_recursive(Qx, Qy)
    (dr, pair_r) = closest_pair_recursive(Rx, Ry)

    if dl < dr:
        d, best_pair = dl, pair_l
    else:
        d, best_pair = dr, pair_r

    (ds, best_pair_split) = closest_split_pair(px, py, d, best_pair)

    if ds < d:
        return ds, best_pair_split
    else:
        return d, best_pair


def closest_pair(points):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_pair_recursive(px, py)


# Генерация случайных точек
def generate_points(n):
    return [(random.randint(0, 10_000), random.randint(0, 10_000)) for _ in range(n)]


# Замер среднего времени
def average_time(trials=5, n=1000):
    total_time = 0
    for _ in range(trials):
        points = generate_points(n)
        start = time.perf_counter()
        dist, pair = closest_pair(points)
        end = time.perf_counter()
        total_time += (end - start)
    avg = total_time / trials
    print(f"Среднее время для n={n}: {avg:.6f} сек")
    return avg


# Построение графика
def plot_runtime():
    sizes = [100, 300, 500, 1000, 2000, 4000]
    times = [average_time(n=n, trials=5) for n in sizes]
    plt.plot(sizes, times, marker='o')
    plt.title("Время работы алгоритма поиска ближайшей пары (разделяй и властвуй)")
    plt.xlabel("Количество точек (n)")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()


plot_runtime()
