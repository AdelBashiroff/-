import time


# Рекурсивная функция для нахождения НОД двух чисел
def recursive_gcd(a, b):
    if b == 0:
        return a
    else:
        return recursive_gcd(b, a % b)


# Функция для оценки времени работы алгоритма
def average_runtime(trials=10, a=123456, b=789012):
    times = []

    for _ in range(trials):
        start = time.perf_counter()
        result = recursive_gcd(a, b)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    avg_time = sum(times) / trials
    print(f"Среднее время выполнения на {trials} запусков: {avg_time:.8f} секунд")
    print(f"НОД({a}, {b}) = {result}")


# Пример вызова
average_runtime()
