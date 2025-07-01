import time
import matplotlib.pyplot as plt


def has_duplicates_set(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False


def has_duplicates_naive(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


def measure_time(func, lst, repeats=5):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.time()
        result = func(lst)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times)


sizes = [10, 100, 500, 1000, 2000, 5000, 10_000, 20_000]
times_set = []
times_naive = []

for size in sizes:
    arr = list(np.random.randint(0, size * 2, size))
    arr.append(arr[0])

    # Замер для множества
    result_set, time_set = measure_time(has_duplicates_set, arr)
    times_set.append(time_set)

    # Замер для двойного цикла (для всех размеров)
    result_naive, time_naive = measure_time(has_duplicates_naive, arr)
    times_naive.append(time_naive)

    print(f"Размер: {size:>6} | Множество: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

plt.figure(figsize=(12, 7))
plt.plot(sizes, times_set, label="Множество (O(n))", marker="o", color="green")
plt.plot(sizes, times_naive, label="Двойной цикл (O(n²))", marker="s", color="red")

plt.title("Сравнение времени проверки дубликатов")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.xscale("linear")
plt.yscale("linear")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()