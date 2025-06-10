# вариант буквы А
n = int(input())
maximum = 0
result = 0
for i in range(1, n+1):
    a = int(input())
    if a >= maximum:
        result = i
        maximum = a
print(result)

# вариант буквы Б
n = int(input())
minimum = 10**9
result = 0
for i in range(1, n+1):
    a = int(input())
    if a <= minimum:
        result = i
        minimum = a
print(result)