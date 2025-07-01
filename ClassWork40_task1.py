import random
import time
import math
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull


def generate_points(n):
    return [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(n)]


def euclidean(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def find_furthest_pair(points):
    max_dist = 0
    pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = euclidean(points[i], points[j])
            if d > max_dist:
                max_dist = d
                pair = (points[i], points[j])
    return pair, max_dist


def is_on_hull(point, hull_points):
    return point in hull_points


def test_and_time(n=300):
    points = generate_points(n)
    start = time.perf_counter()

    # Поиск самых удаленных точек
    (p1, p2), dist = find_furthest_pair(points)

    # Поиск выпуклой оболочки
    hull = ConvexHull(points)
    hull_points = [tuple(points[i]) for i in hull.vertices]

    # Проверка
    result = is_on_hull(p1, hull_points) and is_on_hull(p2, hull_points)

    end = time.perf_counter()
    return result, end - start


# Повторим 10 раз и посчитаем среднее время
def average_time(trials=10, n=300):
    total_time = 0
    for _ in range(trials):
        _, t = test_and_time(n)
        total_time += t
    avg = total_time / trials
    print(f"Среднее время для n={n}: {avg:.6f} сек")
    return avg


# График времени от числа точек
def plot_runtime():
    sizes = [50, 100, 200, 300, 500]
    times = [average_time(n=n, trials=5) for n in sizes]
    plt.plot(sizes, times, marker='o')
    plt.title("Время проверки принадлежности точек оболочке")
    plt.xlabel("Число точек (n)")
    plt.ylabel("Среднее время (сек)")
    plt.grid(True)
    plt.show()


plot_runtime()
