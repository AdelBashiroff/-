import numpy as np
import time
import matplotlib.pyplot as plt

#без NumPy
def max_of_means(matrix):
    max_mean = 10**(-8)
    for row in matrix:
        row_mean = sum(row) / len(row)
        if row_mean > max_mean:
            max_mean = row_mean
    return max_mean

#с NumPy
def numpy_max_of_means(matrix_np):
    return np.max(np.mean(matrix_np, axis=1))
    
#для измерения времени выполнения    
def measure_time(func, matrix, repeats=5):
    if repeats <= 0:
        raise ValueError("Количество повторений должно быть больше 0")

    times = []
    result = None

    for _ in range(repeats):
        start_time = time.time()
        result = func(matrix)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times), min(times), max(times)

sizes = [5, 10, 50, 100, 1000, 10_000, 20_000]

times_numpy_mean = []
times_numpy_min = []
times_numpy_max = []

times_list_mean = []
times_list_min = []
times_list_max = []

for size in sizes:
    N, M = size, size
    A = np.random.randint(1, 10, size=(N, M))
    A_list = A.tolist()
    max_average_numpy, mean_time_numpy, min_time_numpy, max_time_numpy = measure_time(numpy_max_of_means, A, repeats=5)
    times_numpy_mean.append(mean_time_numpy)
    times_numpy_min.append(min_time_numpy)
    times_numpy_max.append(max_time_numpy)
    max_average_list, mean_time_list, min_time_list, max_time_list = measure_time(max_of_means, A_list, repeats=5)
    times_list_mean.append(mean_time_list)
    times_list_min.append(min_time_list)
    times_list_max.append(max_time_list)
    print(f"Размер матрицы: {size}x{size}")
    print(f"Максимальное среднее арифметическое для NumPy массива: {average_numpy}")
    print(f"Среднее время выполнения для NumPy массива: {mean_time_numpy:.7f} секунд")
    print(f"Минимальное время выполнения для NumPy массива: {min_time_numpy:.7f} секунд")
    print(f"Максимальное время выполнения для NumPy массива: {max_time_numpy:.7f} секунд")
    print()

    print(f"Максимальное среднее арифметическое для списка: {average_list}")
    print(f"Среднее время выполнения для списка: {mean_time_list:.7f} секунд")
    print(f"Минимальное время выполнения для списка: {min_time_list:.7f} секунд")
    print(f"Максимальное время выполнения для списка: {max_time_list:.7f} секунд")
    print()

# Построение графика
plt.figure(figsize=(10, 6)) #Создаем фигуру (окно для графика) с размером 10x6 дюймов
plt.plot(sizes, times_numpy_mean, label="NumPy (среднее)", marker="o")
plt.plot(sizes, times_list_mean, label="Список (среднее)", marker="o")
plt.title("Зависимость времени выполнения от размера матрицы")
plt.legend()
plt.grid(True)
# Устанавливаем логарифмическую шкалу для осей X и Y
plt.xscale("log")
plt.yscale("log")

# Отображаем график
plt.show()
