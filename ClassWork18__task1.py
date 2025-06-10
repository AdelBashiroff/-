import random

numbers = [random.randint(1, 100) for _ in range(10)]

print("Случайные числа:", numbers)

max_num = max(numbers)
min_num = min(numbers)

print("Самое большое число:", max_num)
print("Самое маленькое число:", min_num)