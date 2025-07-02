import numpy as np
import time
import matplotlib.pyplot as plt

from statistics import mean

# Функция без NumPy
def manual_max_of_row_means(matrix):
    max_mean = float('-inf')
    for row in matrix:
        row_mean = sum(row) / len(row)
        if row_mean > max_mean:
            max_mean = row_mean
    return max_mean

# Функция с NumPy
def numpy_max_of_row_means(matrix_np):
    return np.max(np.mean(matrix_np, axis=1))

# Размеры матриц для тестирования
sizes = [10, 100, 200, 400, 600, 800, 1000]
repeats = 10

manual_times = []
numpy_times = []

for size in sizes:
    manual_t = []
    numpy_t = []

    for _ in range(repeats):
        # Генерация случайной матрицы
        matrix = [[np.random.randint(0, 1000) for _ in range(size)] for _ in range(size)]
        matrix_np = np.array(matrix)

        # Без NumPy
        start = time.time()
        manual_max_of_row_means(matrix)
        end = time.time()
        manual_t.append(end - start)

        # С NumPy
        start = time.time()
        numpy_max_of_row_means(matrix_np)
        end = time.time()
        numpy_t.append(end - start)

    # Сохраняем среднее время
    manual_times.append({
        "min": min(manual_t),
        "max": max(manual_t),
        "avg": mean(manual_t)
    })

    numpy_times.append({
        "min": min(numpy_t),
        "max": max(numpy_t),
        "avg": mean(numpy_t)
    })

# ------------------------------
# Печать таблицы результатов
# ------------------------------

print(f"{'Size':>6} | {'Manual (avg)':>12} | {'Manual (min)':>12} | {'Manual (max)':>12} || {'NumPy (avg)':>12} | {'NumPy (min)':>12} | {'NumPy (max)':>12}")
print("-" * 90)
for i, size in enumerate(sizes):
    print(f"{size:6} | {manual_times[i]['avg']:.6f}     | {manual_times[i]['min']:.6f}     | {manual_times[i]['max']:.6f}     || {numpy_times[i]['avg']:.6f}     | {numpy_times[i]['min']:.6f}     | {numpy_times[i]['max']:.6f}")

# ------------------------------
# Построение графика
# ------------------------------

plt.figure(figsize=(10, 6))
plt.plot(sizes, [m['avg'] for m in manual_times], label="Manual (avg)", marker='o')
plt.plot(sizes, [m['avg'] for m in numpy_times], label="NumPy (avg)", marker='o')
plt.xlabel("Matrix size (N = M)")
plt.ylabel("Average Time (seconds)")
plt.title("Сравнение скорости: NumPy vs обычный Python")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
