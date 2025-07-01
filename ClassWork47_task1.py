import itertools


def generate_sequences(n, k):
    # Генерация всех последовательностей длины k из чисел от 1 до n
    sequences = itertools.product(range(1, n + 1), repeat=k)

    # Печать каждой последовательности
    for seq in sequences:
        print(seq)


# Пример использования:
n = 3  # Максимальное число
k = 2  # Длина последовательности
generate_sequences(n, k)
